from django.urls import path



from PARTIENT_DOCTOR_MATCHING.django_channel_consummers.consumer import Consumer


websocket_urlpatterns = [
    
    path('ws/meeting/<str:meeting_id>/', Consumer.as_asgi()),
]