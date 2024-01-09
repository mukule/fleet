from django.shortcuts import render, redirect
from .models import Inspection
from car.models import Car
from .forms import InspectionForm
from django.core.mail import *
from django.conf import settings
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.shortcuts import get_object_or_404


def render_to_pdf(template_path, context_dict):
    template = get_template(template_path)
    html = template.render(context_dict)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="inspection_report.pdf"'

    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def inspection(request):
    if request.method == 'POST':
        form = InspectionForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form data
            inspection_instance = form.save()

            # Obtain the related Car instance
            car_instance = get_object_or_404(
                Car, id=inspection_instance.car.id)

            # Update the car's mileage
            car_instance.mileage = form.cleaned_data['current_mileage']

            # Save the updated car instance
            car_instance.save()

            # Create a PDF using ReportLab
            pdf_template_path = 'inspection/inspection_email_template.html'
            pdf_context = {'inspection_instance': inspection_instance}
            pdf_attachment = render_to_pdf(pdf_template_path, pdf_context)

            # Prepare email content using a template
            subject = 'New Inspection Form Submission'
            email_template_name = 'inspection/inspection_email_template.html'
            context = {'form': form}
            message = render_to_string(email_template_name, context)

            # Send email with form details and PDF attachment
            from_email = settings.EMAIL_FROM
            recipient_list = ['info@topstarcarhire.co.ke']

            email = EmailMessage(subject, message, from_email, recipient_list)
            email.attach('inspection_report.pdf',
                         pdf_attachment.content, 'application/pdf')
            email.send()

            # Redirect or render success page
            return redirect('inspection:success')
    else:
        form = InspectionForm()

    return render(request, 'inspection/index.html', {'form': form})


def inspections(request):
    inspections = Inspection.objects.all()
    context = {
        'inspections': inspections
    }
    return render(request, 'inspection/inspections.html', context)


def success(request):
    return render(request, 'inspection/success.html')
