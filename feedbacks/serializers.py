from datetime import datetime
from calendar import timegm
import json

from django.contrib.auth.forms import PasswordResetForm
from django.conf import settings
from django.utils.translation import gettext as _
from rest_framework import serializers
from django.utils.timezone import now

from .models import (
    Complaint,
    SurveyQuestion,
    SurveyAnswer
)

class ComplaintSerializer(serializers.ModelSerializer):

    class Meta:
        model = Complaint
        fields = '__all__'


class SurveyQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = SurveyQuestion
        fields = '__all__'


class SurveyAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = SurveyAnswer
        fields = '__all__'