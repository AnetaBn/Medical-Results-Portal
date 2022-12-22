from django.db import models


class Doctor(models.Model):
    doctor_id = models.BigAutoField(primary_key=True)
    doctor_name = models.CharField(max_length=50, blank=True, null=True)
    specialization = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'doctor'


class Patient(models.Model):
    patient_id = models.BigAutoField(primary_key=True)
    patient_pesel = models.CharField(max_length=50, blank=True, null=True)
    patient_name = models.CharField(max_length=50, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'patient'


class Study(models.Model):
    study_id = models.BigAutoField(primary_key=True)
    hospital = models.CharField(max_length=64, blank=True, null=True)
    study_date = models.DateField(blank=True, null=True)
    modality = models.CharField(max_length=10, blank=True, null=True)
    pathfile = models.CharField(db_column='pathFile', max_length=100, blank=True, null=True)
    patient = models.ForeignKey(Patient, models.DO_NOTHING, blank=True, null=True)
    doctor = models.ForeignKey(Doctor, models.DO_NOTHING, blank=True, null=True)
    image = models.ImageField(upload_to=None, max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'study'
