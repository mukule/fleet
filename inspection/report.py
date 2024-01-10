from django.template.loader import render_to_string
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO
from reportlab.lib import colors
from reportlab.platypus import *
from reportlab.lib.styles import *


def generate_pdf(inspection_instance):
    # Create a BytesIO buffer to receive the PDF data.
    buffer = BytesIO()

    # Create the PDF object, using the BytesIO buffer as its "file."
    pdf = canvas.Canvas(buffer, pagesize=letter)

    # Set font and size for the title
    pdf.setFont("Helvetica-Bold", 16)

    logo_path = 'https://topstarcarhire.co.ke/logo_2d.jpg'
    logo = Image(logo_path, width=100, height=100)
    logo_x = (letter[0] - logo.drawWidth) / 2
    logo.drawOn(pdf, logo_x, 700)  # Adjusted position

    # Calculate the width of the title for centering
    title_text = 'Topstar Car Hire Vehicle Inspection'
    title_width = pdf.stringWidth(title_text, "Helvetica-Bold", 16)
    title_x = (letter[0] - title_width) / 2  # Centered

    # Draw the title
    pdf.drawString(title_x, 670, title_text)

    # Set font and size for the content
    pdf.setFont("Helvetica", 12)

    # Calculate the width of car and date for centering
    car_date_text = f'{inspection_instance.car} - {inspection_instance.date.strftime("%Y-%m-%d")}'
    car_date_width = pdf.stringWidth(car_date_text, "Helvetica", 12)
    car_date_x = (letter[0] - car_date_width) / 2  # Centered

    # Draw car and date
    pdf.drawString(car_date_x, 650, car_date_text)

    # Move down to make space for the table
   

    # Draw the table slightly above to provide space
    table_data = [
        ['Vehicle Mileage:', str(inspection_instance.current_mileage) + ' miles'],
        ['Service Tag:', inspection_instance.service_tag],
        ['Next Service Due:', str(inspection_instance.next_service_due)],
        ['Insurance Expiry:', str(inspection_instance.insurance_expiry)],
        ['Fuel Tank Level:', str(inspection_instance.fuel_tank_level)],
        ['Emergency Equipments:', ', '.join(str(equipment) for equipment in inspection_instance.emergency_equipment.all())],
    ]

    # Define style for the table with reduced padding
    table_style = TableStyle([
        ('LEFTPADDING', (0, 0), (-1, -1), 6),  # Reduced left padding
        ('RIGHTPADDING', (0, 0), (-1, -1), 1),  # Reduced right padding
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ])

    # Calculate the available width for the table
    table_width = letter[0] - 2 * 60  # Reduce left and right padding

    table = Table(table_data, colWidths=[table_width * 0.4, table_width * 0.6], style=table_style)

    # Draw the table on the canvas
    table.wrapOn(pdf, table_width, 200)
    table.drawOn(pdf, 60, 530)  # Adjusted position

  

    first_heading_text = 'Essential Fluid Check'
    first_heading_width = pdf.stringWidth(first_heading_text, "Helvetica-Bold", 16)
    first_heading_x = (letter[0] - first_heading_width) / 2  # Centered

    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(first_heading_x, 500, first_heading_text)


    # Draw the second table
    second_table_data = [
        ['Oil Level Check:', ', '.join(str(oil_check) for oil_check in inspection_instance.oil_level.all())],
        ['Brake Fluid:', ', '.join(str(fluid) for fluid in inspection_instance.brake_fluid.all())],
        ['Power Steering:', ', '.join(str(fluid) for fluid in inspection_instance.power_steering_fluid.all())],
        ['Clutch Fluid:', ', '.join(str(fluid) for fluid in inspection_instance.clutch_fluid.all())],
        ['Auto Transmission Fluid:', ', '.join(str(fluid) for fluid in inspection_instance.auto_transmission_fluid.all())],
        ['Radiator Fluid Level:', ', '.join(str(fluid) for fluid in inspection_instance.radiator_fluid_level.all())],
        ['Windshield Washer Level:', ', '.join(str(fluid) for fluid in inspection_instance.windshield_washer_level.all())],
    ]

    # Define style for the second table with reduced padding
    second_table_style = TableStyle([
        ('LEFTPADDING', (0, 0), (-1, -1), 6),  # Reduced left padding
        ('RIGHTPADDING', (0, 0), (-1, -1), 1),  # Reduced right padding
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ])

    # Calculate the available width for the second table
    second_table_width = letter[0] - 2 * 60  # Reduce left and right padding

    second_table = Table(second_table_data, colWidths=[table_width * 0.4, table_width * 0.6], style=table_style)

    # Draw the second table on the canvas
    second_table.wrapOn(pdf, second_table_width, 200)
    second_table.drawOn(pdf, 60, 350)

  
    second_heading_text = 'Battery Condition'
    second_heading_width = pdf.stringWidth(second_heading_text, "Helvetica-Bold", 16)
    second_heading_x = (letter[0] - second_heading_width) / 2  # Centered

    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(second_heading_x, 320, second_heading_text)

    # Draw the third table
    third_table_data = [
        ['Voltage Recorded:', inspection_instance.voltage_recorded],
        ['Terminals Checked & Tightened:', ', '.join(str(terminal) for terminal in inspection_instance.terminals_checked_and_tightened.all())],
        ['Battery Fluid:', ', '.join(str(fluid) for fluid in inspection_instance.battery_fluid.all())],
    ]

    # Define style for the third table with reduced padding
    third_table_style = TableStyle([
        ('LEFTPADDING', (0, 0), (-1, -1), 6),  # Reduced left padding
        ('RIGHTPADDING', (0, 0), (-1, -1), 1),  # Reduced right padding
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ])

    # Calculate the available width for the third table
    third_table_width = letter[0] - 2 * 60  # Reduce left and right padding

    third_table = Table(third_table_data, colWidths=[third_table_width * 0.4, third_table_width * 0.6], style=third_table_style)

  
    # Draw the third table on the canvas
    third_table.wrapOn(pdf, third_table_width, 200)
    third_table.drawOn(pdf, 60, 250)  # Adjusted position

    

    third_heading_text = 'Vehicle Electronics'
    third_heading_width = pdf.stringWidth(third_heading_text, "Helvetica-Bold", 16)
    third_heading_x = (letter[0] - third_heading_width) / 2  # Centered

    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(third_heading_x, 220, third_heading_text)

    # Draw the fourth table
    fourth_table_data = [
        ['Headlights Working:', ', '.join(str(fluid) for fluid in inspection_instance.headlights_working.all())],
        ['High Beam Working:', ', '.join(str(fluid) for fluid in inspection_instance.high_beam_working.all())],
        ['Brake Lights Working:', ', '.join(str(fluid) for fluid in inspection_instance.brake_lights_working.all())],
        ['Indicators Working:', ', '.join(str(fluid) for fluid in inspection_instance.indicators_working.all())],
        ['Reverse Lights Working:', ', '.join(str(fluid) for fluid in inspection_instance.reverse_lights_working.all())],
        ['Fog Lights Working:', ', '.join(str(fluid) for fluid in inspection_instance.fog_lights_working.all())],
    ]

    # Define style for the fourth table with reduced padding
    fourth_table_style = TableStyle([
        ('LEFTPADDING', (0, 0), (-1, -1), 6),  # Reduced left padding
        ('RIGHTPADDING', (0, 0), (-1, -1), 1),  # Reduced right padding
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ])

    # Calculate the available width for the fourth table
    fourth_table_width = letter[0] - 2 * 60  # Reduce left and right padding

    fourth_table = Table(fourth_table_data, colWidths=[fourth_table_width * 0.4, fourth_table_width * 0.6], style=fourth_table_style)

    # Draw the fourth table on the canvas
    fourth_table.wrapOn(pdf, fourth_table_width, 340)
    fourth_table.drawOn(pdf, 60, 100)  # Adjusted position

    pdf.showPage()

    fifth_heading_text = 'Tyre Conditions'
    fifth_heading_width = pdf.stringWidth(fifth_heading_text, "Helvetica-Bold", 16)
    fifth_heading_x = (letter[0] - fifth_heading_width) / 2  # Centered

    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(fifth_heading_x, 750, fifth_heading_text)

    # Draw the fifth table with three columns
    fifth_table_data = [
        ['Tyre', 'Tire Brand', 'Tire Condition'],
        ['Front Right:', inspection_instance.fr_tire_brand, inspection_instance.fr_tire_condition],
        ['Front Left:', inspection_instance.fl_tire_brand, inspection_instance.fl_tire_condition],
        ['Rear Right:', inspection_instance.rr_tire_brand, inspection_instance.rr_tire_condition],
        ['Rear Left:', inspection_instance.rl_tire_brand, inspection_instance.rl_tire_condition],
        ['Spare:', inspection_instance.spare_tire_brand, inspection_instance.spare_tire_condition],
    ]

    # Define style for the fifth table with reduced padding
    fifth_table_style = TableStyle([
        ('LEFTPADDING', (0, 0), (-1, -1), 6),  # Reduced left padding
        ('RIGHTPADDING', (0, 0), (-1, -1), 1),  # Reduced right padding
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ])

    # Calculate the available width for the fifth table
    fifth_table_width = letter[0] - 2 * 60  # Reduce left and right padding

    fifth_table = Table(fifth_table_data, colWidths=[fifth_table_width * 0.3, fifth_table_width * 0.4, fifth_table_width * 0.3], style=fifth_table_style)

    # Draw the fifth table on the canvas
    fifth_table.wrapOn(pdf, fifth_table_width, 680)
    fifth_table.drawOn(pdf, 60, 630)  # Adjusted position

    # Draw the sixth table
    sixth_heading_text = 'Internal'
    sixth_heading_width = pdf.stringWidth(sixth_heading_text, "Helvetica-Bold", 16)
    sixth_heading_x = (letter[0] - sixth_heading_width) / 2  # Centered

    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(sixth_heading_x, 610, sixth_heading_text)

    # Draw the sixth table with three columns
    sixth_table_data = [
        ['Air Conditioning Working:', ', '.join(str(choice) for choice in inspection_instance.air_conditioning_working.all())],
        ['Radio Working:', ', '.join(str(choice) for choice in inspection_instance.radio_working.all())],
        ['CD:', ', '.join(str(choice) for choice in inspection_instance.CD.all())],
        ['USB:', ', '.join(str(choice) for choice in inspection_instance.USB.all())],
        ['AUX:', ', '.join(str(choice) for choice in inspection_instance.AUX.all())],
        ['FM Expander:', ', '.join(str(choice) for choice in inspection_instance.FM_Expander.all())],
        ['Windscreen Condition:', ', '.join(str(choice) for choice in inspection_instance.windscreen_condition.all())],
        ['Wipers Working:', ', '.join(str(choice) for choice in inspection_instance.wipers_working.all())],
        ['Seat Belts Functioning:', ', '.join(str(choice) for choice in inspection_instance.seat_belts_functioning.all())],
        ['Electric Mirrors Functioning:', ', '.join(str(choice) for choice in inspection_instance.electric_mirrors_functioning.all())],
        ['Electric Windows Functioning:', ', '.join(str(choice) for choice in inspection_instance.electric_windows_functioning.all())],
    ]

    # Define style for the sixth table with reduced padding
    sixth_table_style = TableStyle([
        ('LEFTPADDING', (0, 0), (-1, -1), 6),  # Reduced left padding
        ('RIGHTPADDING', (0, 0), (-1, -1), 1),  # Reduced right padding
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ])

    # Calculate the available width for the sixth table
    sixth_table_width = letter[0] - 2 * 60  # Reduce left and right padding

    sixth_table = Table(sixth_table_data, colWidths=[sixth_table_width * 0.5, sixth_table_width * 0.5], style=sixth_table_style)

    # Draw the sixth table on the canvas
    sixth_table.wrapOn(pdf, sixth_table_width, 680)
    sixth_table.drawOn(pdf, 60, 400)  # Adjusted position

    # Draw the seventh table
    seventh_heading_text = "Driver's Details"
    seventh_heading_width = pdf.stringWidth(seventh_heading_text, "Helvetica-Bold", 16)
    seventh_heading_x = (letter[0] - seventh_heading_width) / 2  # Centered

    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(seventh_heading_x, 370, seventh_heading_text)

    # Draw the seventh table with two columns
    seventh_table_data = [
        ['First Name', 'Last Name'],
        [inspection_instance.first_name, inspection_instance.last_name],
    ]

    # Define style for the seventh table with reduced padding
    seventh_table_style = TableStyle([
        ('LEFTPADDING', (0, 0), (-1, -1), 6),  # Reduced left padding
        ('RIGHTPADDING', (0, 0), (-1, -1), 1),  # Reduced right padding
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ])

    # Calculate the available width for the seventh table
    seventh_table_width = letter[0] - 2 * 60  # Reduce left and right padding

    seventh_table = Table(seventh_table_data, colWidths=[seventh_table_width * 0.5, seventh_table_width * 0.5], style=seventh_table_style)

    # Draw the seventh table on the canvas
    seventh_table.wrapOn(pdf, seventh_table_width, 680)
    seventh_table.drawOn(pdf, 60, 320)  # Adjusted position

    # Draw the eighth table
    eighth_heading_text = "Inspector's Details"
    eighth_heading_width = pdf.stringWidth(eighth_heading_text, "Helvetica-Bold", 16)
    eighth_heading_x = (letter[0] - eighth_heading_width) / 2  # Centered

    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(eighth_heading_x, 300, eighth_heading_text)

    # Draw the eighth table with two columns
    eighth_table_data = [
        ['First Name', 'Last Name'],
        [inspection_instance.inspectors_first_name, inspection_instance.inspectors_last_name],
    ]

    # Define style for the eighth table with reduced padding
    eighth_table_style = TableStyle([
        ('LEFTPADDING', (0, 0), (-1, -1), 6),  # Reduced left padding
        ('RIGHTPADDING', (0, 0), (-1, -1), 1),  # Reduced right padding
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ])

    # Calculate the available width for the eighth table
    eighth_table_width = letter[0] - 2 * 60  # Reduce left and right padding

    eighth_table = Table(eighth_table_data, colWidths=[eighth_table_width * 0.5, eighth_table_width * 0.5], style=eighth_table_style)

    # Draw the eighth table on the canvas
    eighth_table.wrapOn(pdf, eighth_table_width, 680)
    eighth_table.drawOn(pdf, 60, 250)  # Adjusted position

# Draw the eleventh table with Additional Comments and Images side by side
    # Draw 'Additional Comments'
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(60, 200, 'Additional Comments')

    # Draw the actual comments below
    pdf.setFont("Helvetica", 12)
    pdf.drawString(60, 180, inspection_instance.additional_comments)

    # Check if 'dashboard_image' is not empty before attempting to draw
    if inspection_instance.dashboard_image:
        dashboard_image = Image(inspection_instance.dashboard_image.path, width=150, height=100)
        dashboard_image.drawOn(pdf, 60, 150)  # Adjusted position

    # Check if 'car_damage_images' is not empty before attempting to draw
    if inspection_instance.car_damage_images:
        car_damage_images = Image(inspection_instance.car_damage_images.path, width=150, height=100)
        car_damage_images.drawOn(pdf, 210, 150)  # Adjusted position


    # Save the PDF to the BytesIO buffer.
    pdf.showPage()  # Start a new page for additional content (if any)
    pdf.save()

    # Use the BytesIO buffer to get the value of the PDF file.
    pdf_output = buffer.getvalue()

    # Close the buffer.
    buffer.close()

    return pdf_output
