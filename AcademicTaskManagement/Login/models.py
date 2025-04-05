from django.db import models

# Create your models here.

class signup_details(models.Model):
    name = models.CharField(max_length=50, null=False , blank=False)
    surname = models.CharField(max_length=50, null=False, blank=False)
    username = models.CharField(max_length=50, null=False, blank=False)
    password = models.CharField(max_length=20)


class login_details(models.Model):
    user = models.CharField(max_length=50)
    passw = models.CharField(max_length=20)
    signUp_details = models.ForeignKey(signup_details, on_delete= models.CASCADE)

class task(models.Model):
    taskType = models.CharField(max_length=50 ,null=False)
    taskTittle = models.CharField(max_length=100, null=False)
    subDate = models.DateField()
    taskDesc = models.CharField(max_length=255)
    taskReminder = models.CharField(max_length=10)
    signUp_details = models.ForeignKey(signup_details, on_delete= models.CASCADE)
    
    

    