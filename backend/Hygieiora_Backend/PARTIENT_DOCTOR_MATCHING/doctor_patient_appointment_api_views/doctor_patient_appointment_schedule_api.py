#Third-party modules
import random
import string
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework import status
from rest_framework.generics import CreateAPIView

#Django modules 
from django.core.mail import send_mail
from django.conf import settings

#User-defined modules
from ..serializers.doctor_patient_appointment_schedule_serializer import AppointmentSerializer
from ..models import Appointment

@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class CreateAppointment(CreateAPIView):
     
    serializer_class = AppointmentSerializer

    def get_patient_email(self,requestobject):
        user = requestobject.user

        if user.is_authenticated:
        # 'user' is authenticated, retrieve email from the database
            email = user.email
            full_name = user.full_name
            return email,full_name 
        else:
        # User is not authenticated
            return None 
        

    def generate_meeting_id(self, length=6):
        characters = string.digits + string.ascii_letters
        return ''.join(random.choice(characters) for _ in range(length))

    def send_appointment_confirmation_email(self, appointment):
        doctor_name = appointment.doctor_name
        patient_name = appointment.patient_name
        meeting_id = appointment.meeting_id
        

        subject = 'Appointment Confirmation'
        message = (f"Dear {patient_name},\n\n"
                   f"Your appointment with Dr. {doctor_name} has been confirmed.\n"
                   f"Meeting ID: {meeting_id}")
        
        from_email = settings.DEFAULT_FROM_EMAIL  # Use the default from_email from settings
        recipient_list = [appointment.patient_email]

        send_mail(subject, message, from_email, recipient_list)

    def post(self, request, format=None):
        patient_details = self.get_patient_email(request)
        if patient_details :
            data = request.data.copy()
            data.setdefault('doctor_name', request.POST.get("docter_name"))
            data.setdefault('patient_name', patient_details[1])
            data.setdefault('meeting_id', self.generate_meeting_id())
            data.setdefault('patient_email', patient_details[0])
            serializer = self.get_serializer(data=data)
            if serializer.is_valid():
                appointment = serializer.save()
                self.send_appointment_confirmation_email(appointment)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



