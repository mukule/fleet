# Generated by Django 4.2.3 on 2023-08-10 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0015_carout_alter_reservation_total_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='carout',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='carout',
            name='card_expiry',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='carout',
            name='country_of_issue',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='carout',
            name='credit_card',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='carout',
            name='credit_card_number',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='carout',
            name='drivers_license_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='carout',
            name='full_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='carout',
            name='ld_appt_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='carout',
            name='license_expiry',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='carout',
            name='mobile_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='carout',
            name='nationality',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='carout',
            name='office_telephone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='carout',
            name='physical_address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='carout',
            name='residence_address',
            field=models.TextField(blank=True, null=True),
        ),
    ]
