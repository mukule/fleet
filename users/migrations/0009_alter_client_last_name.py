# Generated by Django 4.2.3 on 2023-12-01 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_client_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='last_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]