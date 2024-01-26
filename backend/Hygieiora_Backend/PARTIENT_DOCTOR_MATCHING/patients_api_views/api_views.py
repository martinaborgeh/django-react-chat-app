#Third-party modules
from rest_framework import generics
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404

#Django modules


#Custom created modules
from ..serializers.patient_serializers import SymptomSerializer,DiseaseSerializer,DoctorSerializer
from ..models import SymptomDetails,Disease
from accounts.models import Doctor


class SearchbySymptom(APIView):
  
    """Retrieve"""

    #permission_classes = [IsAuthenticated,]
    
    def get_object(self, pk, symptom=None):
        try:
            if pk:
                return SymptomDetails.objects.get(pk=pk)
            elif symptom:
                return SymptomDetails.objects.filter(symptom=symptom)
            else:
                return []
        except SymptomDetails.DoesNotExist:
            return 404
        except Exception as e:
            # Handle other unexpected exceptions (internal server errors)
             return 500

    def get(self, request, pk=None, symptom=None, format=None):
        symptoms = self.get_object(pk=pk, symptom=symptom)
        if symptoms == 404:
           error_message = "search by symptoms not found."
           return Response({"error": error_message,"data": []},status=status.HTTP_404_NOT_FOUND) 

       # Handle internal server errors
        elif symptoms == 500:
            error_message = "Internal server error occurred."
            return Response({"error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

       # Handle eror if search results is empty
        elif not symptoms:
            error_message = "search by symptoms not found"
            return Response({"error": error_message,"data": []},status=status.HTTP_404_NOT_FOUND)
       
       # Handle successful data retrieval        
        else:
            serializer = SymptomSerializer(symptoms, many=True)
            success_message = "search by symptom(s) retrieved successfully."
            return Response({"success": success_message, "data": serializer.data}, status=status.HTTP_200_OK)
        


class SearchbyDisease(APIView):

   """Retrieve"""
    
   #permission_classes = [IsAuthenticated,]
   
   def get_object(self, pk, disease=None):
       try:
           if pk:
               return Disease.objects.get(pk=pk)
           elif disease:
               return Disease.objects.filter(disease=disease)
           else:
               return []
       except Disease.DoesNotExist:
           return 404
       except Exception as e:
            # Handle other unexpected exceptions (internal server errors)
            return 500
   
   def get(self, request, pk=None, disease=None, format=None):
       diseases = self.get_object(pk=pk, disease=disease)
       
       # Handle the case when object Does not
       if diseases == 404:
           error_message = "search by Disease not found. "
           return Response({"error": error_message},status=status.HTTP_404_NOT_FOUND) 

       # Handle internal server errors
       elif diseases == 500:
           error_message = "Internal server error occurred."
           return Response({"error": error_message,"data": []}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

       # Handle eror if search results is empty
       elif not diseases:
           error_message = "search by Disease not found"
           return Response({"error": error_message,"data": []},status=status.HTTP_404_NOT_FOUND)
       
       # Handle successful data retrieval        
       else:
           serializer = DiseaseSerializer(diseases, many=True)
           success_message = "search by Disease(s) retrieved successfully."
           return Response({"success": success_message, "data": serializer.data}, status=status.HTTP_200_OK)


class SearchbyDoctor(APIView):

    """Retrieve"""

    #permission_classes = [IsAuthenticated,]

    def get_object(self, pk, email=None):
        try:
            if pk:
                return Doctor.objects.get(pk=pk)
            elif email:
                print(get_object_or_404(Doctor, user__email=email))
                return get_object_or_404(Doctor, user__email=email)
            else:
                return []
        except Doctor.DoesNotExist:
           return 404
        except Exception as e:
            # Handle other unexpected exceptions (internal server errors)
            return 500

    def get(self, request, pk=None, email=None, format=None):
        doctor = self.get_object(pk=pk, email=email)
 
       
       # Handle the case when object Does not
        if doctor == 404:
            error_message = "search by doctor not found."
            return Response({"error": error_message,"data": []},status=status.HTTP_404_NOT_FOUND) 

       # Handle internal server errors
        elif doctor == 500:
            error_message = "Internal server error occurred."
            return Response({"error": error_message,"data": []}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

       # Handle eror if search results is empty
        elif not doctor:
            error_message = "search by doctor not found"
            return Response({"error": error_message,"data": []},status=status.HTTP_404_NOT_FOUND)
       
       # Handle successful data retrieval        
        else:
            serializer = DoctorSerializer(doctor)
            success_message = "search by doctor(s) retrieved successfully."
            return Response({"success": success_message, "data": serializer.data}, status=status.HTTP_200_OK)

        

class SearchbySpecialization(APIView):

    """Retrieve"""

    #permission_classes = [IsAuthenticated,]
   
    def get_object(self, pk, specialization=None):
       
        
        try:
            if pk:
                return Doctor.objects.get(pk=pk)
            elif specialization:
                return Doctor.objects.filter(specialization=specialization)
            else:
                return []
        except Doctor.DoesNotExist:
           return 404
        except Exception as e:
            # Handle other unexpected exceptions (internal server errors)
            return 500         

    def get(self, request, pk=None, specialization=None, format=None):
        specializations = self.get_object(pk=pk, specialization=specialization)
       
       # Handle the case when object Does not
        if specializations == 404:
            error_message = "search by specialization not found."
            return Response({"error": error_message,"data": []},status=status.HTTP_404_NOT_FOUND) 

       # Handle internal server errors
        elif specializations == 500:
            error_message = "Internal server error occurred."
            return Response({"error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

       # Handle eror if search results is empty
        elif not specializations:
            error_message = "search by specialization not found"
            return Response({"error": error_message,"data": []},status=status.HTTP_404_NOT_FOUND)
       
       # Handle successful data retrieval        
        else:
            serializer = DoctorSerializer(specializations, many=True)
            success_message = "search by specialization(s) retrieved successfully."
            return Response({"success": success_message, "data": serializer.data}, status=status.HTTP_200_OK)


