from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class EmployeeDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    empcode = models.CharField(max_length=20)
    managercode = models.CharField(max_length=20, null=True)
    designation = models.CharField(max_length=20, null=True)
    gender = models.CharField(max_length=10, null=True)
    user_type = models.CharField(max_length=20, default='employee')  # Add this line

    
    def __str__(self):
        return self.user.username
