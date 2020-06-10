from django.shortcuts import render
from django.db.models import Q

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets, status
from rest_framework_extensions.mixins import NestedViewSetMixin

from django_filters.rest_framework import DjangoFilterBackend

from feedbacks.models import (
    Complaint,
    SurveyQuestion,
    SurveyAnswer
)

from feedbacks.serializers import (
    ComplaintSerializer,
    SurveyQuestionSerializer,
    SurveyAnswerSerializer
)

class ComplaintViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    

    
    def get_queryset(self):
        queryset = Complaint.objects.all()

        """
        if self.request.user.is_anonymous:
            queryset = Company.objects.none()

        else:
            user = self.request.user
            company_employee = CompanyEmployee.objects.filter(employee=user)
            company = company_employee[0].company
            
            if company.company_type == 'AD':
                queryset = Organisation.objects.all()
            else:
                queryset = Organisation.objects.filter(company=company.id)
        """
        return queryset  

    @action(methods=['GET'], detail=True)
    def in_progress(self, request, *args, **kwargs):
        complaint = self.get_object()
        complaint.status = 'IP'
        complaint.save()

        serializer = ComplaintSerializer(complaint)
        return Response(serializer.data)

    @action(methods=['GET'], detail=True)
    def completed(self, request, *args, **kwargs):
        complaint = self.get_object()
        complaint.status = 'CM'
        complaint.save()

        serializer = ComplaintSerializer(complaint)
        return Response(serializer.data)
 

class SurveyQuestionViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = SurveyQuestion.objects.all()
    serializer_class = SurveyQuestionSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    

    
    def get_queryset(self):
        queryset = SurveyQuestion.objects.all()

        """
        if self.request.user.is_anonymous:
            queryset = Company.objects.none()

        else:
            user = self.request.user
            company_employee = CompanyEmployee.objects.filter(employee=user)
            company = company_employee[0].company
            
            if company.company_type == 'AD':
                queryset = Organisation.objects.all()
            else:
                queryset = Organisation.objects.filter(company=company.id)
        """
        return queryset    
 

class SurveyAnswerViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = SurveyAnswer.objects.all()
    serializer_class = SurveyAnswerSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    

    
    def get_queryset(self):
        queryset = SurveyAnswer.objects.all()

        """
        if self.request.user.is_anonymous:
            queryset = Company.objects.none()

        else:
            user = self.request.user
            company_employee = CompanyEmployee.objects.filter(employee=user)
            company = company_employee[0].company
            
            if company.company_type == 'AD':
                queryset = Organisation.objects.all()
            else:
                queryset = Organisation.objects.filter(company=company.id)
        """
        return queryset    
 
 