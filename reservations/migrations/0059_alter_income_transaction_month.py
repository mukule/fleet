# Generated by Django 4.2.3 on 2023-12-28 12:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0058_alter_income_transaction_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='transaction_month',
            field=models.DateField(default=datetime.datetime(2023, 12, 28, 12, 43, 2, 981774, tzinfo=datetime.timezone.utc)),
        ),
    ]