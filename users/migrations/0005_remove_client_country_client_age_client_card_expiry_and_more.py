# Generated by Django 4.2.3 on 2023-08-10 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_driver_client_company_client_country_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='country',
        ),
        migrations.AddField(
            model_name='client',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='card_expiry',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='country_of_issue',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='credit_card',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='credit_card_number',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='drivers_license_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='license_expiry',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='nationality',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='office_telephone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='physical_address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='residence_address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
