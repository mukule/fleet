# Generated by Django 4.2.3 on 2023-10-01 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0044_alter_carout_fuel_in_alter_carout_fuel_out'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='contract_generated',
            field=models.BooleanField(default=False),
        ),
    ]
