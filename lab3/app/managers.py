from django.db import models
from django.utils import timezone

class PatientManager(models.Manager):
    def find_by_accident_date(self, date):
        return self.filter(medical_encounters__date=date)

    def find_by_care_provider(self, care_provider_name):
        return self.filter(medical_encounters__care_provider__name=care_provider_name)

class CareProviderManager(models.Manager):
    def find_by_health_issue(self, health_issue_type):
        return self.filter(medicalencounter__healthservice__health_issue__type=health_issue_type)
