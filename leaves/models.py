from django.db import models
import datetime
from django.contrib.auth.models import User



#from Hello.home.models import Employee  # Incorrect app name or case


class Employee(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    employee_name = models.CharField(max_length=255)
    employee_username = models.CharField(max_length=255)
    employee_password = models.CharField(max_length=255)
    employee_mobile = models.CharField(max_length=15)
    employee_manager_id = models.IntegerField()
    employee_type = models.CharField(max_length=50)

    def __str__(self):
        return self.employee_name

class Manager(models.Model):
    manager_id = models.IntegerField(primary_key=True)
    manager_name = models.CharField(max_length=255)
    manager_username = models.CharField(max_length=255)
    manager_password = models.CharField(max_length=255)
    manager_mobile = models.CharField(max_length=15)

    def __str__(self):
        return self.manager_name

class Leave(models.Model):
    leave_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    employee_name = models.CharField(max_length=255, default="")
    leave_type = models.CharField(max_length=50)
    leave_description = models.TextField()
    leave_from = models.DateField()
    leave_to = models.DateField()
    proof_attachment = models.FileField(upload_to='proof_attachments/', default='default_proof_attachment.pdf')
    application_date = models.DateField(default=datetime.date.today)

    def __str__(self):
         return f"{self.employee_name} - {self.leave_type}"
    


