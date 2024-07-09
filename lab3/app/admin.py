from django.contrib import admin
from .models import CareProvider,MedicalEncounter,HealthIssue,Patient,HealthService
# Register your models here.
admin.site.register(CareProvider)
admin.site.register(MedicalEncounter)
admin.site.register(HealthIssue)
admin.site.register(Patient)
admin.site.register(HealthService)
