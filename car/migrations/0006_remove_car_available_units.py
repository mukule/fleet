# Generated by Django 4.2.3 on 2023-07-24 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0005_alter_car_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='available_units',
        ),
    ]
