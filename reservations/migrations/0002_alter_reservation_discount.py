# Generated by Django 4.2.3 on 2023-07-25 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, null=True),
        ),
    ]
