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


def inspection(request):
    if request.method == 'POST':
        form = InspectionForm(request.POST, request.FILES)
        if form.is_valid():
            inspection_instance = form.save(commit=False)
            car_instance = get_object_or_404(
                Car, id=inspection_instance.car.id)
            car_instance.mileage = form.cleaned_data['current_mileage']
            car_instance.save()

            # Save the inspection instance to get an ID for the many-to-many relationships
            inspection_instance.save()

            # Handle ManyToMany relationships
            inspection_instance.emergency_equipment.set(
                form.cleaned_data['emergency_equipment'])
            inspection_instance.oil_level.set(form.cleaned_data['oil_level'])
            inspection_instance.brake_fluid.set(
                form.cleaned_data['brake_fluid'])
            inspection_instance.power_steering_fluid.set(
                form.cleaned_data['power_steering_fluid'])
            inspection_instance.clutch_fluid.set(
                form.cleaned_data['clutch_fluid'])
            inspection_instance.auto_transmission_fluid.set(
                form.cleaned_data['auto_transmission_fluid'])
            inspection_instance.radiator_fluid_level.set(
                form.cleaned_data['radiator_fluid_level'])
            inspection_instance.windshield_washer_level.set(
                form.cleaned_data['windshield_washer_level'])
            inspection_instance.terminals_checked_and_tightened.set(
                form.cleaned_data['terminals_checked_and_tightened'])
            inspection_instance.battery_fluid.set(
                form.cleaned_data['battery_fluid'])
            inspection_instance.headlights_working.set(
                form.cleaned_data['headlights_working'])
            inspection_instance.high_beam_working.set(
                form.cleaned_data['high_beam_working'])
            inspection_instance.brake_lights_working.set(
                form.cleaned_data['brake_lights_working'])
            inspection_instance.indicators_working.set(
                form.cleaned_data['indicators_working'])
            inspection_instance.reverse_lights_working.set(
                form.cleaned_data['reverse_lights_working'])
            inspection_instance.fog_lights_working.set(
                form.cleaned_data['fog_lights_working'])
            inspection_instance.air_conditioning_working.set(
                form.cleaned_data['air_conditioning_working'])
            inspection_instance.radio_working.set(
                form.cleaned_data['radio_working'])
            inspection_instance.CD.set(
                form.cleaned_data['CD'])
            inspection_instance.USB.set(
                form.cleaned_data['USB'])
            inspection_instance.AUX.set(
                form.cleaned_data['AUX'])
            inspection_instance.FM_Expander.set(
                form.cleaned_data['FM_Expander'])
            inspection_instance.windscreen_condition.set(
                form.cleaned_data['windscreen_condition'])
            inspection_instance.seat_belts_functioning.set(
                form.cleaned_data['seat_belts_functioning'])
            inspection_instance.electric_mirrors_functioning.set(
                form.cleaned_data['electric_mirrors_functioning'])
            inspection_instance.electric_windows_functioning.set(
                form.cleaned_data['electric_windows_functioning'])

            if request.FILES.getlist('car_damage_images'):
                try:
                    first_damage_image = DamageImage(
                        inspection=inspection_instance, d_image=request.FILES.getlist('car_damage_images')[0])
                    first_damage_image.save()
                except ValidationError as e:

                    pass

            # Save all uploaded images to DamageImage model
            for image_file in request.FILES.getlist('car_damage_images')[1:]:
                try:
                    DamageImage.objects.create(
                        inspection=inspection_instance,
                        d_image=image_file
                    )
                except ValidationError as e:
                    pass
            # Create a PDF using ReportLab
            pdf_attachment = generate_pdf(inspection_instance)

            # Prepare email content
            subject = f'New Vehicle Inspection for {car_instance}'
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
                # Handle email sending error
                # Log the error or take appropriate action
                pass
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
