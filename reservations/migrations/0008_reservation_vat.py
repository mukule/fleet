# Generated by Django 4.2.3 on 2023-07-29 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0007_taxes'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='vat',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, null=True),
        ),
    ]
