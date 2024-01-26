#Third-party modules
from rest_framework import serializers

#Django modules

#Custom-created modules
from ..models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    doctor_name =  serializers.CharField(required =True)
    patient_name =  serializers.CharField(required =True)
    meeting_id = serializers.CharField(required =True)
    patient_email = serializers.EmailField(required =True)

    class Meta:
        model = Appointment
        fields  = ['id', 'doctor_name', 'patient_name','meeting_id','patient_email']
