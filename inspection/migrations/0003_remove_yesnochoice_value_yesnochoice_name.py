# Generated by Django 4.2.3 on 2023-12-26 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0002_fluidstatuschoice_yesnochoice_remove_inspection_aux_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yesnochoice',
            name='value',
        ),
        migrations.AddField(
            model_name='yesnochoice',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
