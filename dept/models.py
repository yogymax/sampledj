from django.db import models

# Create your models here.

class Dept(models.Model):
    deptName=models.CharField('DEPT_NAME',max_length=30)
    deptCode=models.CharField('DEPT_CODE',max_length=10,unique=True)
    deptRemarks=models.TextField('DEPT_REMR',max_length=100)
    class Meta:
        db_table='Dept_Info'

