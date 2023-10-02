from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from django.shortcuts import get_object_or_404
from reservations.models import Reservation
import io
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def invoices(request):
    search_query = request.GET.get('search')

    # Fetch all reservations and order them by the date they were created
    reservations = Reservation.objects.all().order_by('-created_at')

    # Apply filter if search query is provided
    if search_query:
        reservations = reservations.filter(
            Q(reservation_number__icontains=search_query) |
            Q(client__first_name__icontains=search_query) |
            Q(client__last_name__icontains=search_query)
        )

    # Configure pagination
    page_number = request.GET.get('page', 1)
    items_per_page = 10
    paginator = Paginator(reservations, items_per_page)

    try:
        reservations = paginator.page(page_number)
    except PageNotAnInteger:
        reservations = paginator.page(1)
    except EmptyPage:
        reservations = paginator.page(paginator.num_pages)

    # Pass the reservations and pagination to the template context
    context = {'reservations': reservations}
    return render(request, 'invoices/invoice.html', context)





def invoice_detail(request, reservation_id):
    # Get the specific reservation using reservation_id
    reservation = get_object_or_404(Reservation, pk=reservation_id)

    # Pass the reservation to the template context
    context = {'reservation': reservation}
    return render(request, 'invoices/invoice_detail.html', context)
