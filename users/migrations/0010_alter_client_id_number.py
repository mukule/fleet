# Generated by Django 4.2.3 on 2023-12-01 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_client_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='id_number',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
