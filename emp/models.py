from django.db import models

# Create your models here.

class Emp(models.Model):
    empName=models.CharField('EMP_NAME',max_length=30)
    empSal=models.FloatField('EMP_SAL',)
    empAge=models.IntegerField('EMP_AGE',)
    empAddress=models.CharField('EMP_ADR',max_length=10,unique=True)
    empDesig=models.TextField('EMP_DES',max_length=100)
    class Meta:
        db_table='Emp_Info'
