from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dept_name = models.CharField(max_length=50)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.CharField(max_length=50)
    hire_date = models.DateField()

    def __str__(self):
        return self.first_name
    

# Create your models here.
