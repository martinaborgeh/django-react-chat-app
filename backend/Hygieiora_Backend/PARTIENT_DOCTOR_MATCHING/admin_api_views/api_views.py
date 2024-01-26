#Third party models
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

#Django models
from django.shortcuts import render

#Custom Created
from serializers.admin_serializers import SymptomSerializer,DrugSerializer
from ..models import SymptomDetails,DrugsDetails
from ..../accounts.permissions import IsOwnerOrReadOnly

#Symptoms admin views
##Get or Create all symptom  instances
class CreateOrGetallSymptomAllSympton(generics.ListCreateAPIView):
    queryset = SymptomDetails.objects.all()
    permission_classes = (IsAdminUser, IsOwnerOrReadOnly)
    serializer_class = SymptomSerializer

##Get ,update, destroy single  symptom  instance
class RetrieveOrUpdateOrDestroySymptom(generics.RetrieveUpdateDestroyAPIView):
    queryset = SymptomDetails.objects.all()
    permission_classes = (IsAdminUser, IsOwnerOrReadOnly)
    serializer_class = SymptomSerializer


#Drug  admin views

##Get or create all symptom  instances
class CreateOrGetallSymptomAllDrug(generics.ListCreateAPIView):
    queryset = DrugsDetails.objects.all()
    permission_classes = (IsAdminUser, IsOwnerOrReadOnly)
    serializer_class = DrugSerializer

##Get ,update, destrol single  symptom  instance
class RetrieveOrUpdateOrDestroyDrug(generics.RetrieveUpdateDestroyAPIView):
    queryset = DrugsDetails.objects.all()
    permission_classes = (IsAdminUser, IsOwnerOrReadOnly)
    serializer_class = DrugSerializer