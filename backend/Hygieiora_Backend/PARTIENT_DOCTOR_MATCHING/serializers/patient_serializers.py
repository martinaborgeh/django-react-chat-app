#Third-party modules
from rest_framework import serializers

#Django modules

#Custom-created modules
from ..models import SymptomDetails,Disease
from accounts.models import Doctor

#Doctor model Serialize
class DoctorSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='user.full_name', read_only=True)
    class Meta:
        model = Doctor
        fields  = ['id', 'full_name', 'specialization','availability','location']


#Symptom model Serializer
class SymptomSerializer(serializers.ModelSerializer):
    doctor= DoctorSerializer(many=True, read_only=True, source='doctor_assigned') #appending doctors information
    class Meta:
        model = SymptomDetails
        fields = ['id', 'doctor', 'symptom']

#Disease model Serializer
class DiseaseSerializer(serializers.ModelSerializer):
    doctor= DoctorSerializer(read_only=True, source='doctor_assigned') #appending doctors information
    class Meta:
        model = Disease
        fields = ['id', 'doctor','disease']





