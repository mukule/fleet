# Generated by Django 4.2.3 on 2023-08-20 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0016_insurance_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insurance',
            name='duration',
            field=models.CharField(choices=[('', 'Select Duration'), ('1M', '1 Month'), ('1Y', '1 Year')], max_length=2, null=True),
        ),
    ]
