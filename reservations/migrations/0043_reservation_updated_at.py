# Generated by Django 4.2.3 on 2023-09-02 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0042_carout_o_country_of_issue_carout_o_drivers_dl_expiry_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
