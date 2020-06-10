# Generated by Django 2.2 on 2020-06-10 19:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('feedbacks', '0003_auto_20200610_1830'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_patient', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('mrn', models.CharField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('patient_type', models.CharField(choices=[('IN', 'Inpatient'), ('OUT', 'Outpatient')], default='IN', max_length=2)),
                ('feedback_type', models.CharField(choices=[('01', 'How get to know IJN'), ('02', 'Access and waiting time'), ('03', 'Information and communication'), ('04', 'Patient and family rights'), ('05', 'Confidence in health professionals'), ('06', 'Safety of environment'), ('07', 'Hygience and cleaniness'), ('08', 'Food and beverages'), ('09', 'Meet expectations?'), ('10', 'Recommend IJN'), ('11', 'Best experience'), ('12', 'Suggestion for improvement')], default='01', max_length=2)),
                ('feedback', models.CharField(max_length=100, null=True)),
                ('waiting_type', models.CharField(choices=[('AD', 'Admission'), ('DC', 'Discharge')], default='AD', max_length=2)),
                ('is_acceptable', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='complaint',
            name='complaint',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='complaint_category',
            field=models.CharField(choices=[('TX', 'Text'), ('VB', 'Verbal'), ('NA', 'Not Available')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='location',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='phone',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='surveyanswer',
            name='answer',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='surveyquestion',
            name='category',
            field=models.CharField(choices=[('IN', 'Internal'), ('EX', 'External'), ('NA', 'Not Available')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='surveyquestion',
            name='question',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='surveyquestion',
            name='survey_type',
            field=models.CharField(choices=[('SR', 'Star Rating'), ('MC', 'Multiple Choice'), ('FT', 'Free Text'), ('NS', 'Net Promoter Score'), ('TU', 'Thums Up/Down'), ('EM', 'Emoji'), ('NA', 'Not Available')], max_length=2, null=True),
        ),
    ]
