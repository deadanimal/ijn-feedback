# Generated by Django 2.2 on 2020-06-10 18:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('feedbacks', '0002_auto_20200610_0925'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='complainer_type',
            field=models.CharField(choices=[('PT', 'Patient'), ('VS', 'Visitor'), ('ST', 'Staff')], default='PT', max_length=2),
        ),
        migrations.AddField(
            model_name='complaint',
            name='complaint_behaviour',
            field=models.CharField(choices=[('AP', 'Appearance'), ('AT', 'Attitude')], default='AT', max_length=2),
        ),
        migrations.AddField(
            model_name='complaint',
            name='complaint_class',
            field=models.CharField(choices=[('PP', 'People'), ('PC', 'Process'), ('FC', 'Facilities')], default='PP', max_length=2),
        ),
        migrations.AddField(
            model_name='complaint',
            name='complaint_department',
            field=models.CharField(choices=[('ST', 'Staff'), ('SC', 'Security'), ('CN', 'Cleaner'), ('UT', 'UTKKKM'), ('OT', 'Others'), ('OP', 'Outler Operators')], default='ST', max_length=2),
        ),
        migrations.AddField(
            model_name='complaint',
            name='complaint_position',
            field=models.CharField(choices=[('DR', 'Doctor'), ('NS', 'Nurse'), ('CT', 'Counter')], default='DR', max_length=2),
        ),
        migrations.AddField(
            model_name='complaint',
            name='date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='complaint',
            name='location',
            field=models.CharField(default='NA', max_length=255),
        ),
    ]
