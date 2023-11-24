# Create your models here.
from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    salary = models.IntegerField(default=0)
    address = models.CharField(max_length=100)

    class Meta:
        db_table = "tblemployee"