# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid

from django.contrib.gis.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from simple_history.models import HistoricalRecords

from core.helpers import PathAndRename

from users.models import (
    CustomUser
)

class Complaint(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, default='NA')
    email = models.CharField(max_length=100, default='NA')
    phone = models.CharField(max_length=100, default='NA')
    complaint = models.TextField(default='NA')
    complaint_to = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, related_name='complaint_to')

    COMPLAINER_TYPE = [
        ('PT', 'Patient'),
        ('VS', 'Visitor'),
        ('ST', 'Staff')
    ]
    complainer_type = models.CharField(
        max_length=2,
        choices=COMPLAINER_TYPE,
        default='PT'
    )

    location = models.CharField(max_length=255, default='NA')
    date = models.DateTimeField(blank=True)

    COMPLAINT_CLASS = [
        ('PP', 'People'),
        ('PC', 'Process'),
        ('FC', 'Facilities')
    ]
    complaint_class = models.CharField(
        max_length=2,
        choices=COMPLAINT_CLASS,
        default='PP'
    )

    COMPLAINT_DEPARTMENT = [
        ('ST', 'Staff'),
        ('SC', 'Security'),
        ('CN', 'Cleaner'),
        ('UT', 'UTKKKM'),
        ('OT', 'Others'),
        ('OP', 'Outler Operators')
    ]
    complaint_department = models.CharField(
        max_length=2,
        choices=COMPLAINT_DEPARTMENT,
        default='ST'
    )

    COMPLAINT_POSITION = [
        ('DR', 'Doctor'),
        ('NS', 'Nurse'),
        ('CT', 'Counter')
    ]
    complaint_position = models.CharField(
        max_length=2,
        choices=COMPLAINT_POSITION,
        default='DR'
    )

    COMPLAINT_BEHAVIOR = [
        ('AP', 'Appearance'),
        ('AT', 'Attitude')
    ]
    complaint_behaviour = models.CharField(
        max_length=2,
        choices=COMPLAINT_BEHAVIOR,
        default='AT'
    )

    COMPLAINT_CATEGORY = [
        ('TX', 'Text'),
        ('VB', 'Verbal'),
        ('NA', 'Not Available')
    ]
    complaint_category = models.CharField(
        max_length=2,
        choices=COMPLAINT_CATEGORY,
        default='NA'
    )
    supporting_docs = models.FileField(null=True, upload_to=PathAndRename('docs'))

    STATUS = [
        ('SB', 'Submitted'),
        ('IP', 'In Progress'),
        ('CM', 'Completed')
    ]
    status = models.CharField(
        max_length=2,
        choices=STATUS,
        default='SB'
    )

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name


class SurveyQuestion(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question = models.CharField(max_length=100, default='NA')
    
    CATEGORY = [
        ('IN', 'Internal'),
        ('EX', 'External'),
        ('NA', 'Not Available')
    ]
    category = models.CharField(
        max_length=2,
        choices=CATEGORY,
        default='NA'
    )

    SURVEY_TYPE = [
        ('SR', 'Star Rating'),
        ('MC', 'Multiple Choice'),
        ('FT', 'Free Text'),
        ('NS', 'Net Promoter Score'),
        ('TU', 'Thums Up/Down'),
        ('EM', 'Emoji'),
        ('NA', 'Not Available'),
    ]
    survey_type = models.CharField(
        max_length=2,
        choices=SURVEY_TYPE,
        default='NA'
    )

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['question']
    
    def __str__(self):
        return self.question


class SurveyAnswer(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    answer = models.CharField(max_length=100, default='NA')
    question = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE)
    by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, related_name='survey_answer_by')

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['question']
    
    def __str__(self):
        return self.question

