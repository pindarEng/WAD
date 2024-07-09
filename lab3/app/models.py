from django.db import models
from .managers import CareProviderManager, PatientManager
# Create your models here.
class MedicalEncounter(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField("date")
    patient = models.ForeignKey('Patient',on_delete=models.CASCADE,related_name='medical_encounters')
    care_provider = models.ForeignKey('CareProvider',on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.patient.name}-{self.date}"

    
class CareProvider(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    specialty = models.CharField(max_length=100)
    objects = CareProviderManager()
    def __str__(self):
        return self.name

class HealthService(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=200)
    type = models.CharField(max_length=100)
    health_issue = models.ForeignKey('HealthIssue',on_delete=models.CASCADE,related_name='health_services')
    medical_encounter = models.ForeignKey('MedicalEncounter',on_delete=models.CASCADE)

    def __str__(self):
        return self.description

class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    objects = PatientManager()
    
    def __str__(self):
        return self.name


class HealthIssue(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100)
    patient = models.ForeignKey('Patient',on_delete=models.CASCADE, related_name="health_issues")
    def __str__(self):
        return self.type