# Generated by Django 2.2 on 2020-06-10 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('OP', 'Open'), ('CS', 'Close')], default='OP', max_length=2),
        ),
    ]
