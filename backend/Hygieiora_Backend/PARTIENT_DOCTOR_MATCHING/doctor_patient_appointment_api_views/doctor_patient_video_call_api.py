#Third-party modules
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from rest_framework import serializers, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

#Custom created modules
from ..serializers.doctor_patient_video_call_serializer import StartCallSerializer,MessageModelSerializer,JoinCallSerializer
from accounts.models import CustomUser
from accounts.permissions import IsOwnerOrReadOnly 
from ..models import Appointment

@authentication_classes([JWTAuthentication])
@permission_classes([IsOwnerOrReadOnly ])

class StartCall(APIView):
    def get_doctors_email(self, requestobject):
        user = requestobject.user

        if user.is_authenticated:
            # 'user' is authenticated, retrieve email from the database
            email = user.email
            full_name = user.full_name
            return email, full_name
        else:
            # User is not authenticated
            return None

    def post(self, request, format=None):
        meeting_id = request.data.get("meeting_id")  # Use 'data' instead of 'POST' for DRF
        get_meeting_id = Appointment.objects.filter(meeting_id=meeting_id)
        doctors_detail = self.get_doctors_email(request)

        if meeting_id and get_meeting_id and doctors_detail:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)

    # Add more fields as needed

@authentication_classes([JWTAuthentication])
@permission_classes([IsOwnerOrReadOnly ])
class NotifyNewCall(APIView):
    def get_doctors_email(self, requestobject):
        user = requestobject.user

        if user.is_authenticated:
            # 'user' is authenticated, retrieve email from the database
            return True
        else:
            # User is not authenticated
            return None

    def post(self, request, format=None):
        doctors_detail = self.get_doctors_email(request)
        meeting_id = request.data['meeting_id']
        print("meeting id is ",meeting_id)
        print('ff',request.data['meeting_id'])

        if doctors_detail:
            channel_layer = get_channel_layer()

                # Send message to the group 'chat_{meeting_id}'
            async_to_sync(channel_layer.group_send)(
                  f'chat_{meeting_id}', {
                        'type': 'new_user_notification',
                        'message': "You started a new meeting"
                        
                    }
                )
            return Response({"message:welcome to chatroom"},status=status.HTTP_200_OK)
            
        else:
            return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)

@authentication_classes([JWTAuthentication])
@permission_classes([IsOwnerOrReadOnly ])
class SendMessage(APIView):
    def get_doctors_email(self, requestobject):
        user = requestobject.user

        if user.is_authenticated:
            # 'user' is authenticated, retrieve email from the database
            return True
        else:
            # User is not authenticated
            return None

    def post(self, request, format=None):
        doctors_detail = self.get_doctors_email(request)
        meeting_id = request.data['meeting_id']
        send_message = request.data['send_message']
                                        
        

        if doctors_detail:
            channel_layer = get_channel_layer()

                # Send message to the group 'chat_{meeting_id}'
            async_to_sync(channel_layer.group_send)(
                  f'chat_{meeting_id}', {
                        'type': 'new_message',
                        'message': send_message
                        
                    }
                )
            return Response({"message:welcome to chatroom"},status=status.HTTP_200_OK)
            
        else:
            return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)


@authentication_classes([JWTAuthentication])
@permission_classes([IsOwnerOrReadOnly ])
class EndCall(APIView):
    def get_doctors_email(self, requestobject):
        user = requestobject.user

        if user.is_authenticated:
            # 'user' is authenticated, retrieve email from the database
            return True
        else:
            # User is not authenticated
            return None

    def post(self, request, format=None):
        print(request.data)
        doctors_detail = self.get_doctors_email(request)
      
        meeting_id = request.data['meeting_id']
     
        if doctors_detail:
            channel_layer = get_channel_layer()

                # Send message to the group 'chat_{meeting_id}'
            async_to_sync(channel_layer.group_send)(
                  f'chat_{meeting_id}', {
                        'type': 'new_user_notification',
                        'message': "Call ended"
                        
                    }
                )
            return Response({"message:welcome to chatroom"},status=status.HTTP_200_OK)
            
        else:
            return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class JoinCall(APIView):

    #authentication_classes = [JWTAuthentication]
    #permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = JoinCallSerializer(data=request.data)
        if serializer.is_valid():
            user_type = serializer.validated_data['user_type']
            peer_js = serializer.validated_data['peer_js']
            meeting_id = serializer.validated_data['meeting_id']

            # Perform any additional logic based on the serializer data
            # For example, you might want to check if the user has permission to join the meeting

            # Join the user to the call group
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_add)(
                'call_%s' % meeting_id,
                self.scope['user'].channel_name  # Use the user's channel_name as the group member
            )

            # Broadcast a message to notify others about the new participant
            async_to_sync(channel_layer.group_send)(
                'call_%s' % meeting_id, {
                    'type': 'new_participant',
                    'message': {
                        'user_type': user_type,
                        'peer_js': peer_js,
                        'user_id': self.scope['user'].id,
                        'username': self.scope['user'].username,
                    }
                }
            )

            return Response({'message': 'Successfully joined the meeting'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


