# Generated by Django 5.1.4 on 2024-12-05 17:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentorship', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='course',
        ),
        migrations.RemoveField(
            model_name='student',
            name='status',
        ),
        migrations.AlterField(
            model_name='mentor',
            name='courses',
            field=models.ManyToManyField(related_name='mentors', to='mentorship.course'),
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('ongoing', 'Ongoing'), ('completed', 'Completed'), ('stopped', 'Stopped')], default='ongoing', max_length=10)),
                ('enrollment_date', models.DateField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mentorship.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mentorship.student')),
            ],
        ),
    ]
