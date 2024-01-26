#Third-party modules
import datetime

#Django modules
from django.db import models

#Custom-created modules
from accounts.models import Doctor,CustomUser


# Create your models here.
class DrugsDetails(models.Model):
    drug = models.CharField(max_length = 100,verbose_name = "drug name",null =False,blank = False)
    date_created = models.DateTimeField( verbose_name = "date created",null =False,blank = False,default=datetime.datetime.fromtimestamp(0))
    date_supplied = models.DateTimeField(verbose_name = "date supplied",null =False,blank = False,default=datetime.datetime.fromtimestamp(0))
    date_manufactured = models.DateTimeField(verbose_name = "date manufactured",null =False,blank = False,default=datetime.datetime.fromtimestamp(0))
    date_expired = models.DateTimeField(verbose_name = "date expired",null =False,blank = False,default=datetime.datetime.fromtimestamp(0))
    drug_prescription = models.CharField(max_length = 100, verbose_name = "drug prescription",null =False,blank = False)
    def __str__(self):
        return f"{self.drug}"

    class Meta:
        verbose_name = "Drug"
        verbose_name_plural = "Drugs"


class SymptomDetails(models.Model):
    doctor_assigned =  models.ManyToManyField(Doctor,max_length = 100,related_name = "doctor_assigned")
    symptom = models.CharField(max_length = 100,verbose_name = "symptom",null =False,blank = False)
    date_created = models.DateTimeField(verbose_name = "date created",null =False,blank = False,default=datetime.datetime.fromtimestamp(0))
    prescribed_drugs =  models.ManyToManyField(DrugsDetails,related_name = "prescribe_drug")

    def __str__(self):
        return f"{self.symptom}"

    class Meta:
        verbose_name = "Symptom"
        verbose_name_plural = "Symptoms"

class Disease(models.Model):
    disease = models.CharField(max_length = 100,verbose_name = "disease",null =False,blank = False)
    causative_agent = models.CharField(max_length = 100,verbose_name = "causative agent",null =True,blank = True,default=datetime.datetime.fromtimestamp(0))
    date_created = models.DateTimeField(verbose_name = "date created",null =False,blank = False,default=datetime.datetime.fromtimestamp(0))
    prescribed_drugs =  models.ForeignKey(DrugsDetails,on_delete=models.CASCADE,related_name = "disease_prescribe_drug")
    doctor_assigned =  models.ForeignKey(Doctor,max_length = 100,on_delete=models.CASCADE,related_name = "doctor_assigned_to_disease")
    symptoms = models.ForeignKey(SymptomDetails,max_length = 100,on_delete=models.CASCADE,related_name = "disease_symptoms") 

    def __str__(self):
        return f"{self.disease}"

    class Meta:
        verbose_name = "Disease"
        verbose_name_plural = "Diseases"

class DepartmentAdmin(models.Model):
    first_name = models.CharField(max_length = 100,verbose_name = "admin firstname",null =False,blank = False)
    surname = models.CharField(max_length = 100,verbose_name = "admin surname",null =False,blank = False)
    admin_qualification = models.CharField(max_length = 100,verbose_name = "qualification",null =False,blank = False)
    email_address =  models.EmailField(null =False,blank = False)
    contact_number = models.PositiveIntegerField(null =False,blank = False)

    def __str__(self):
        return f"{self.first_name}  {self.surname}"

    class Meta:
        verbose_name = "Department Admin"
        verbose_name_plural = "Department Admins"


class Department(models.Model):
    department = models.CharField(max_length = 100,verbose_name = "department",null =False,blank = False)
    date_created = models.DateTimeField(verbose_name = "date created",null =False,blank = False,default=datetime.datetime.fromtimestamp(0))
    department_admin = models.OneToOneField(DepartmentAdmin,max_length = 100,on_delete=models.CASCADE,related_name = "department_admin",null =False,blank = True)
    doctor_assigned =  models.ForeignKey(Doctor,max_length = 100,on_delete=models.CASCADE,related_name = "doctors_assigned_to_department")
    diseases = models.ForeignKey(Disease,max_length = 100,on_delete=models.CASCADE,related_name = "department_diseases")  
    
    def __str__(self):
        return f"{self.department}"

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"

class Appointment(models.Model):
    doctor_name =  models.CharField(max_length = 100, verbose_name = "doctors name",null = False,blank= False)
    patient_name =  models.CharField(max_length = 100, verbose_name = "doctors name",null = False,blank= False)
    patient_email = models.EmailField(verbose_name = "doctors_email",null = False,blank= False)
    meeting_id = models.CharField(max_length = 100, verbose_name = "doctors name",null = False,blank= False)

    def __str__(self):
        return f"{self.meeting_id}"

    class Meta:
        verbose_name = "Appointment"
        verbose_name_plural = "Appointments"




class Message(models.Model):
    text = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True, blank=True)
    sender = models.ForeignKey(CustomUser, related_name='sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(CustomUser, related_name='receiver', on_delete=models.CASCADE)

    


