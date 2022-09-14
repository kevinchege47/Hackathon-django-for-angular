from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from .models import *
class AllergynameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allergies
        fields = ('allergy_name',)
class DoctorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Doctor
		fields = '__all__'

class AllergiesSerializer(serializers.ModelSerializer):
	allergy_name = AllergynameSerializer(many=True)
	class Meta:
		model = Allergies
		fields = '__all__'

class IllnessesSerializer(serializers.ModelSerializer):

	class Meta:
		model = illnesses
		fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
	class Meta:
		model = Patient
		fields = '__all__'