# Generated by Django 4.2.3 on 2023-07-24 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0003_carmodel_remove_car_make_alter_car_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.DateField(),
        ),
    ]
