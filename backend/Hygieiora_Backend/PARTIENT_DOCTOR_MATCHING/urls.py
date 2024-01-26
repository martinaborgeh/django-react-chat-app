#django modules
from django.urls import path


#Custom created views

from .patients_api_views.api_views import (
SearchbySymptom,
SearchbyDisease,
SearchbyDoctor,
SearchbySpecialization,

)

from .doctor_patient_appointment_api_views.doctor_patient_appointment_schedule_api import CreateAppointment
from .doctor_patient_appointment_api_views.checkifuserisauthorisetoviewthispage import (
CheckifPageisAuthorizetoViewbyDoctor,
CheckifPageisAuthorizetoViewbyPatient
)

from .doctor_patient_appointment_api_views.doctor_patient_video_call_api import (

StartCall,
NotifyNewCall,
SendMessage,
EndCall
)



urlpatterns = [

    #searches
    path('search-by-symptoms/<str:symptom>/', SearchbySymptom.as_view(), name='search-by-symptom'),
    path('search-by-diseases/<str:disease>/', SearchbyDisease.as_view(), name='search-by-disease'),
    path('search-by-doctors-email/<str:email>/', SearchbyDoctor.as_view(), name='search-by-doctor'),
    path('search-by-specializations/<str:specialization>/', SearchbySpecialization.as_view(), name='search-by-specialization'),

    #creating appointment
    path('create-appointment/', CreateAppointment.as_view(), name='create-appointment'), 

    #checking for page view authentication and authorization
    path('check-page-view-is-authorized-for-patient/', CheckifPageisAuthorizetoViewbyPatient.as_view(), name='check-page-view-is-authorized-for-patient'),
    path('check-page-view-is-authorized-for-doctor/', CheckifPageisAuthorizetoViewbyDoctor.as_view(), name='check-page-view-is-authorized-for-doctor'),

    #Doctors and patients appointments
    path('start-call/', StartCall.as_view(), name='start-call'), 
    path('call-welcome-message/', NotifyNewCall.as_view(), name='call-welcome-message'),
    path('send-message/', SendMessage.as_view(), name='send-message'),
    path('end-call/', EndCall.as_view(), name='end-call'),


]
