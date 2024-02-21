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

def handle_file_uploads(request, inspection_instance):
    # Handle the first 3 damage images
    for index, image_file in enumerate(request.FILES.getlist('car_damage_images')):
        if index >= 3:
            break  # Stop processing after the first 3 images
        
        try:
            DamageImage.objects.create(
                inspection=inspection_instance,
                d_image=image_file
            )
        except ValidationError as e:
            # Handle validation error here, if needed
            pass

def generate_and_send_email(inspection_instance, car_instance):
    # Create a PDF using ReportLab
    pdf_attachment = generate_pdf(inspection_instance)

    # Prepare email content
    subject = f'New Vehicle Inspection for {car_instance.model} - {car_instance.year}'
    message = 'Please find the inspection report attached.'

    # Send email with PDF attachment
    from_email = settings.EMAIL_FROM
    recipient_list = ['info@topstarcarhire.co.ke']

    try:
        email = EmailMessage(
            subject, message, from_email, recipient_list)
        email.attach('inspection_report.pdf',
                     pdf_attachment, 'application/pdf')
        email.send()
    except Exception as e:
      
        logger.error(f"Unexpected error: {e}")

def inspection(request):
    if request.method == 'POST':
        form = InspectionForm(request.POST, request.FILES)
        if form.is_valid():
            inspection_instance = form.save(commit=False)
            
           
            car_instance = get_object_or_404(Car, id=inspection_instance.car.id)
            car_instance.mileage = form.cleaned_data['current_mileage']
            car_instance.save()

           
            inspection_instance.save()

          
            handle_many_to_many_fields(inspection_instance, form)
            handle_file_uploads(request, inspection_instance)
            generate_and_send_email(inspection_instance, car_instance)

           
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

def inspection_detail(request, pk):
    inspection = get_object_or_404(Inspection, id=pk)

    context = {
        'inspection': inspection,
    }
    return render(request, 'inspection/inspection_detail.html', context)

def delete_inspection(request, pk):
    inspection = get_object_or_404(Inspection, id=pk)

  
    inspection.delete()
    return redirect('inspection:inspections') 


def success(request):
    return render(request, 'inspection/success.html')
