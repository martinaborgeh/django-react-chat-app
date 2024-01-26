#Django modules
from django.db import models


#Third-party modules
from rest_framework import serializers

#Custom-created modules
from ..models import SymptomDetails,DrugsDetails,Disease,Department,DepartmentAdmin


#Symptom model Serializer
class SymptomSerializer(serializers.ModelSerializer):

   
    symptom = serializers.CharField(required =True)
    date_created = serializers.DateTimeField(required =True)
    
   
    class Meta:
        model = SymptomDetails
        fields = ['id', 'doctor_assigned', 'symptom', 'date_created', 'prescribed_drugs']



#Drug model Serializer
class DrugSerializer(serializers.ModelSerializer):

    drug = serializers.CharField(required=True)
    date_created = serializers.DateTimeField(required =True)
    date_supplied = serializers.DateTimeField(required =True)
    date_manufactured = serializers.DateTimeField(required =True)
    date_expired = serializers.DateTimeField(required =True)
    drug_prescription = serializers.CharField(required =True)

    class Meta:
        model = DrugsDetails
        fields = ['id', 'drug', 'date_created', 'date_supplied', 'date_manufactured', 'date_expired','drug_prescription']



#Disease model Serializer
class DiseaseSerializer(serializers.ModelSerializer):
    disease = serializers.CharField(required =True)
    date_created = serializers.DateTimeField(required =True)
    
    class Meta:
        model = Disease
        fields = ['id', 'disease', 'causative_agent', 'date_created', 'prescribed_drugs','doctor_assigned']

#Department model Serializer
class DepartmentSerializer(serializers.ModelSerializer):
    department = serializers.CharField(required =True)
    date_created = serializers.DateTimeField(required =True)
    

    class Meta:
        model = Department
        fields = ['id', 'department', 'date_created', 'department_admin', 'doctor_assigned', 'diseases']


#Department Admin model Serializer
class DepartmentAdminSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required =True)
    surname = serializers.CharField(required =True)
    admin_qualification = serializers.CharField(required =True)
    email_address =  serializers.EmailField(required =True)
    contact_number = models.PositiveIntegerField(null =False,blank = False)

    class Meta:
        model = DepartmentAdmin
        fields = ['id', 'first_name', 'surname', 'admin_qualification', 'email_address', 'contact_number']

    
    