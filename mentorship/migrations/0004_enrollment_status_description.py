# Generated by Django 5.1.4 on 2024-12-06 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentorship', '0003_remove_student_enrollment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='status_description',
            field=models.CharField(blank=True, help_text='Reason for status', max_length=255, null=True),
        ),
    ]
