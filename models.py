# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Doctor(models.Model):
    doctor_id = models.BigAutoField(primary_key=True)
    doctor_name = models.CharField(max_length=50, blank=True, null=True)
    specialization = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doctor'


class Patient(models.Model):
    patient_id = models.BigAutoField(primary_key=True)
    patient_name = models.CharField(max_length=50, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient'


class Study(models.Model):
    study_id = models.BigAutoField(primary_key=True)
    hospital = models.CharField(max_length=64, blank=True, null=True)
    study_date = models.DateField(blank=True, null=True)
    modality = models.CharField(max_length=10, blank=True, null=True)
    pathfile = models.CharField(db_column='pathFile', max_length=100, blank=True, null=True)  # Field name made lowercase.
    patient = models.ForeignKey(Patient, models.DO_NOTHING, blank=True, null=True)
    doctor = models.ForeignKey(Doctor, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'study'
