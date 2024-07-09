# Generated by Django 5.0.6 on 2024-07-03 15:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CareProvider',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('speciality', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='HealthIssue',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalEncounter',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(verbose_name='date')),
                ('care_provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.careprovider')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medical_encounters', to='app.patient')),
            ],
        ),
        migrations.CreateModel(
            name='HealthService',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=100)),
                ('health_issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='health_services', to='app.healthissue')),
                ('medical_encounter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.medicalencounter')),
            ],
        ),
        migrations.AddField(
            model_name='healthissue',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='health_issues', to='app.patient'),
        ),
    ]
