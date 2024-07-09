from django.core.management.base import BaseCommand
from datetime import datetime
from django.utils import timezone
from app.models import Patient, HealthIssue, HealthService, CareProvider, MedicalEncounter


class Command(BaseCommand):
    help = 'Loads sample data into the database'

    def handle(self, *args, **kwargs):
        self.clear_data()

        # CareProviders
        drJohn = CareProvider.objects.create(name='Dr. John', specialty='Cardiolog')
        drEinstein = CareProvider.objects.create(name='Dr. Einstein', specialty='Terapie Intensiva')

        # Patients
        john = Patient.objects.create(name='John Doe')

        # HealthIssues
        infarct = HealthIssue.objects.create(type='Infarct', patient=john)

        # MedicalEncounters
        encounter1 = MedicalEncounter.objects.create(patient=john, date=timezone.make_aware(datetime(2022, 11, 21)), care_provider=drJohn)
        encounter2 = MedicalEncounter.objects.create(patient=john, date=timezone.make_aware(datetime(2013, 3, 21)), care_provider=drEinstein)


        # HealthServices
        carolDavila = HealthService.objects.create(description='Shock', type='Carol Davila', health_issue=infarct,medical_encounter = encounter1)
        bucurestiUrgente = HealthService.objects.create(description='Urgente', type='Bucuresti Spital Urgente', health_issue=infarct,medical_encounter = encounter2)

        # HealthServices to MedicalEncounters
        # encounter1.health_services.add(carolDavila)
        # encounter2.health_services.add(bucurestiUrgente)

        self.stdout.write(self.style.SUCCESS('SUCCESS'))

        self.query_data()
    
    def query_data(self):
        self.stdout.write(self.style.SUCCESS('\nAll Patients'))
        patients = Patient.objects.all()
        for patient in patients:
            self.stdout.write(str(patient))

        self.stdout.write(self.style.SUCCESS('\nAll Health Issues by John Doe'))
        health_issues_by_patient = HealthIssue.objects.filter(patient__name='John Doe')
        for issue in health_issues_by_patient:
            self.stdout.write(str(issue))

        self.stdout.write(self.style.SUCCESS('\nPatients who had an accident on "2022-11-21"'))
        patients_by_date = Patient.objects.find_by_accident_date(timezone.make_aware(datetime(2022, 11, 21)))
        for patient in patients_by_date:
            self.stdout.write(str(patient))

        self.stdout.write(self.style.SUCCESS('\nPatients who had an accident on "2000-10-24"'))
        patients_by_wrong_date = Patient.objects.find_by_accident_date(timezone.make_aware(datetime(2000, 10, 24)))
        for patient in patients_by_wrong_date:
            self.stdout.write(str(patient))

        self.stdout.write(self.style.SUCCESS('\nPatients who had Dr. Einstein as care provider'))
        patients_met_einstein = Patient.objects.find_by_care_provider('Dr. Einstein')
        for patient in patients_met_einstein:
            self.stdout.write(str(patient))

        self.stdout.write(self.style.SUCCESS('\nCare providers who had patients with infarct'))
        care_providers_by_health_issue = CareProvider.objects.find_by_health_issue('Infarct')
        for provider in care_providers_by_health_issue:
            self.stdout.write(str(provider))



    def clear_data(self):
        # Clear existing data (if needed)
        MedicalEncounter.objects.all().delete()
        HealthService.objects.all().delete()
        HealthIssue.objects.all().delete()
        CareProvider.objects.all().delete()
        Patient.objects.all().delete()
