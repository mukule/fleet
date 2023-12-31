# Generated by Django 4.2.3 on 2023-09-02 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0017_alter_insurance_duration'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carservice',
            old_name='description',
            new_name='service_report',
        ),
        migrations.RemoveField(
            model_name='carservice',
            name='service_company',
        ),
        migrations.AddField(
            model_name='carservice',
            name='current_kms',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='carservice',
            name='next_service',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='carservice',
            name='quantity',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='carservice',
            name='service_by',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='carservice',
            name='service_provider_contacts',
            field=models.TextField(null=True),
        ),
    ]
