from django.db import models

# Create your models here.
class Employee(models.Model):
    #Table creation with makemigrations and migrate
    EmployeeId   = models.CharField(max_length=4)
    EmployeeName =models.CharField(max_length=1000)
    EmployeeDesignation = models.CharField(max_length=1000)
    EmployeeSalary= models.CharField(max_length=10)
    EmployeeMobile = models.CharField(max_length=12)


    #Create / Insert /Add               - POST
    # Retrieve                          - GET
    #Update  Edit with Primary key      - PUT
    #Delete /Remove                     - DELETE               - 