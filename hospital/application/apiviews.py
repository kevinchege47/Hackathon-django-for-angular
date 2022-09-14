from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import *
from .serializers import DoctorSerializer, AllergiesSerializer,IllnessesSerializer,PatientSerializer

class DoctorList(generics.ListCreateAPIView):
	def get_queryset(self):
		queryset = Doctor.objects.all()
        # queryset = Allergies.objects.get(id=pk)
		return queryset
	serializer_class = DoctorSerializer 

class AllergiesList(generics.ListCreateAPIView):
	def get_queryset(self):
		queryset = Allergies.objects.all()
        # queryset = Allergies.objects.get(id=pk)
		return queryset
	serializer_class = AllergiesSerializer
    
class illnessesList(generics.ListCreateAPIView):
	def get_queryset(self):
		queryset = illnesses.objects.all()
        # queryset = Allergies.objects.get(id=pk)
		return queryset
	serializer_class = IllnessesSerializer 

class PatientList(generics.ListCreateAPIView):
	def get_queryset(self):
		queryset = Patient.objects.all()
        # queryset = Allergies.objects.get(id=pk)
		return queryset
	serializer_class = PatientSerializer 
