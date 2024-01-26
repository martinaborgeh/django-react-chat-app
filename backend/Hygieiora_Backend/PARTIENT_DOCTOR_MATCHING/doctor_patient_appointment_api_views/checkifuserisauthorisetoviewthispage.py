#Third-party modules

from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework import status
from rest_framework.generics import CreateAPIView

#Django modules 


#User-defined modules
from accounts.permissions import IsOwnerOrReadOnly 

#Check if patient is authenticated
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])

class CheckifPageisAuthorizetoViewbyPatient(CreateAPIView):

    def check_if_user_is_authenticated(self,requestobject):
        user = requestobject.user
        if user.is_authenticated:
            return True      
        else:
            return False
        
    def post(self, request, format=None):
        print(request)
        patient_details = self.check_if_user_is_authenticated(request)
        if patient_details :     
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


#Check if doctor  is authenticated
@authentication_classes([JWTAuthentication])
@permission_classes([IsOwnerOrReadOnly])

class CheckifPageisAuthorizetoViewbyDoctor(CreateAPIView):

    def check_if_user_is_authenticated(self,requestobject):
        user = requestobject.user
        if user.is_authenticated:
            return True      
        else:
            return False
        
    def post(self, request, format=None):
        patient_details = self.check_if_user_is_authenticated(request)
        if patient_details :     
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

