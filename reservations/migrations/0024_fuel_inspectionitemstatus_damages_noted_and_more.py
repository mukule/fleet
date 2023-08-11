# Generated by Django 4.2.3 on 2023-08-11 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0023_carinspection_inspectionitem_inspectionitemstatus_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fuel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('1/4', '1/4'), ('1/2', '1/2'), ('3/4', '3/4'), ('Full', 'Full')], max_length=5)),
            ],
        ),
        migrations.AddField(
            model_name='inspectionitemstatus',
            name='damages_noted',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='inspectionitemstatus',
            name='kms_allowed',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='inspectionitemstatus',
            name='kms_driven',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='inspectionitemstatus',
            name='kms_in',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='inspectionitemstatus',
            name='kms_out',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='inspectionitemstatus',
            name='fuel_in',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fuel_in', to='reservations.fuel'),
        ),
        migrations.AddField(
            model_name='inspectionitemstatus',
            name='fuel_out',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fuel_out', to='reservations.fuel'),
        ),
    ]