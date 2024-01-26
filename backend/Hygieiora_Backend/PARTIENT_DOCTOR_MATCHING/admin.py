#Django modules
from django.contrib import admin

#Custom-created modules
from .models import SymptomDetails,DrugsDetails,DepartmentAdmin,Department,Disease
from .serializers.admin_serializers import (
SymptomSerializer,
DrugSerializer,
DiseaseSerializer,
DepartmentSerializer,
DepartmentAdminSerializer
)


#Symptom Admin
class SymptomModelAdmin(admin.ModelAdmin):
   
    serializer_class = SymptomSerializer
   
admin.site.register(SymptomDetails, SymptomModelAdmin)


#Drug Admin
class DrugModelAdmin(admin.ModelAdmin):
    
    serializer_class = DrugSerializer
    
admin.site.register(DrugsDetails, DrugModelAdmin)


#Disease Admin
class DiseaseModelAdmin(admin.ModelAdmin):
    
    serializer_class = DiseaseSerializer
    
admin.site.register(Disease, DiseaseModelAdmin)


#Department Admin
class DepartmentModelAdmin(admin.ModelAdmin):
    
    serializer_class = DepartmentSerializer
    
admin.site.register(Department, DepartmentModelAdmin)


#DepartmentAdmin Admin
class DepartmentAdminModelAdmin(admin.ModelAdmin):
    
    serializer_class = DepartmentAdminSerializer
    
admin.site.register(DepartmentAdmin, DepartmentAdminModelAdmin)
