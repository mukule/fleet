from django.shortcuts import render, redirect
from .models import *
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
from django.core.exceptions import ValidationError
import logging

logger = logging.getLogger(__name__)


def handle_many_to_many_fields(inspection_instance, form):
    # Handle ManyToMany relationships
    for field in ['emergency_equipment', 'oil_level', 'brake_fluid', 'power_steering_fluid', 'clutch_fluid', 'auto_transmission_fluid', 'radiator_fluid_level', 'windshield_washer_level', 'terminals_checked_and_tightened', 'battery_fluid', 'headlights_working', 'high_beam_working', 'brake_lights_working', 'indicators_working', 'reverse_lights_working', 'fog_lights_working', 'air_conditioning_working', 'radio_working', 'CD', 'USB', 'AUX', 'FM_Expander', 'windscreen_condition', 'seat_belts_functioning', 'electric_mirrors_functioning', 'electric_windows_functioning']:
        getattr(inspection_instance, field).set(form.cleaned_data[field])

from PIL import Image
from io import BytesIO

def handle_file_uploads(request, inspection_instance, max_file_size=10 * 1024 * 1024, max_width=800, max_height=600, max_quality=85):
    for index, image_file in enumerate(request.FILES.getlist('car_damage_images')):
        # Check file size
        if image_file.size > max_file_size:
            # Handle large file size error here
            pass
        else:
            try:
                image = Image.open(image_file)
                
                # Check dimensions and reduce quality if necessary
                if image.width > max_width or image.height > max_height:
                    image.thumbnail((max_width, max_height), Image.ANTIALIAS)
                
                # Save the image to a BytesIO buffer with reduced quality
                buffer = BytesIO()
                image.save(buffer, format='JPEG', quality=max_quality)
                
                # Create DamageImage object with the optimized image
                DamageImage.objects.create(
                    inspection=inspection_instance,
                    d_image=buffer,
                )
            except Exception as e:
                # Handle any errors that may occur during image processing
                pass


def generate_and_send_email(inspection_instance, car_instance):
    # Create a PDF using ReportLab
    pdf_attachment = generate_pdf(inspection_instance)

    # Prepare email content
    subject = f'New Vehicle Inspection for {car_instance.model} - {car_instance.year}'
    message = 'Please find the inspection report attached.'

    # Send email with PDF attachment
    from_email = settings.EMAIL_FROM
    recipient_list = ['nelsonmasibo6@gmail.com']

    try:
        email = EmailMessage(
            subject, message, from_email, recipient_list)
        email.attach('inspection_report.pdf',
                     pdf_attachment, 'application/pdf')
        email.send()
    except Exception as e:
        # Log or handle unexpected errors
        logger.error(f"Unexpected error: {e}")

def inspection(request):
    if request.method == 'POST':
        form = InspectionForm(request.POST, request.FILES)
        if form.is_valid():
            inspection_instance = form.save(commit=False)
            
            # Get car instance and update mileage
            car_instance = get_object_or_404(Car, id=inspection_instance.car.id)
            car_instance.mileage = form.cleaned_data['current_mileage']
            car_instance.save()

            # Save the inspection instance to get an ID for the many-to-many relationships
            inspection_instance.save()

            # Call the helper functions
            handle_many_to_many_fields(inspection_instance, form)
            handle_file_uploads(request, inspection_instance)
            generate_and_send_email(inspection_instance, car_instance)

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
