#Third-party modules
import datetime
from rest_framework import serializers

#Custom created modules
from PARTIENT_DOCTOR_MATCHING.models import Message



class MessageModelSerializer(serializers.ModelSerializer):
    sender = serializers.CharField(read_only=True, source='sender.username')
    read = serializers.BooleanField(default=True)

    class Meta:
        model = Message
        fields = ('text', 'sender', 'date_time', 'read','receiver')


class JoinCallSerializer(serializers.Serializer):
    peer_js = serializers.CharField()
    user_type = serializers.ChoiceField(choices=('doctor', 'patient'))  # Add more choices if needed
    meeting_id = serializers.CharField()



#class StartCallSerializer(serializers.Serializer):
#    receiver = serializers.CharField()
#    sender = serializers.CharField()
#    peer_id = serializers.CharField()


class StartCallSerializer(serializers.Serializer):
    doctor_email = serializers.CharField()
    doctor_name = serializers.CharField()
    meeting_id = serializers.CharField()