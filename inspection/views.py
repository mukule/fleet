from django.shortcuts import render, redirect
from .models import Inspection
from car.models import Car
from .forms import InspectionForm
from django.core.mail import EmailMessage
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404
from reportlab.pdfgen import canvas
from io import BytesIO
from .report import generate_pdf




def inspection(request):
    if request.method == 'POST':
        form = InspectionForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form data
            inspection_instance = form.save()

            # Obtain the related Car instance
            car_instance = get_object_or_404(Car, id=inspection_instance.car.id)

            # Update the car's mileage
            car_instance.mileage = form.cleaned_data['current_mileage']

            # Save the updated car instance
            car_instance.save()

            # Create a PDF using ReportLab
            pdf_attachment = generate_pdf(inspection_instance)

            # Prepare email content
            subject = f'New Vehicle Inspection for {car_instance}'
            message = 'Please find the inspection report attached.'

            # Send email with PDF attachment
            from_email = settings.EMAIL_FROM
            recipient_list = ['nelsonmasibo6@gmail.com']

            email = EmailMessage(subject, message, from_email, recipient_list)
            email.attach('inspection_report.pdf', pdf_attachment, 'application/pdf')
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
