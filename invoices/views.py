from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from django.shortcuts import get_object_or_404
from reservations.models import Reservation
import io
from xhtml2pdf import pisa


def invoices(request):
    # Fetch all reservations and order them by the date they were created
    reservations = Reservation.objects.all().order_by('-created_at')

    # Pass the reservations to the template context
    context = {'reservations': reservations}
    return render(request, 'invoices/invoice.html', context)


def invoice_detail(request, reservation_id):
    # Get the specific reservation using reservation_id
    reservation = get_object_or_404(Reservation, pk=reservation_id)

    # Pass the reservation to the template context
    context = {'reservation': reservation}
    return render(request, 'invoices/invoice_detail.html', context)



def generate_invoice(request, reservation_id):
    # Get the specific reservation using reservation_id
    reservation = get_object_or_404(Reservation, pk=reservation_id)

    # Load the HTML template
    template = get_template('invoices/invoice_template.html')
    context = {'reservation': reservation}
    html = template.render(context)

    # Create a PDF buffer
    pdf_buffer = io.BytesIO()

    # Convert HTML to PDF using xhtml2pdf
    pdf = pisa.CreatePDF(html, dest=pdf_buffer)

    if not pdf.err:
        # Get the PDF buffer's content and close it
        pdf_content = pdf_buffer.getvalue()
        pdf_buffer.close()

        # Set the response to download the PDF
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'
        response.write(pdf_content)

        return response

    return HttpResponse("Error generating PDF", status=500)