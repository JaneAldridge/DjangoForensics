from django.db import models
from django.contrib.auth.models import User #IMPORTING USER MODEL


# Create your models here.


#USER PROFILE IS AN EXTENSION TO dJANGO'S MODEL OF USERS 

class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dateOfBirth = models.DateField()
    gender = models.CharField(
        max_length=6,
        choices=[('MALE', 'MALE'),('FEMALE', 'FEMALE')]
    )
    departmentName = models.CharField(
        max_length=100,
        choices=[('Name 1', 'Name 1'),('Name 2', 'Name 2'),('Name 3', 'Name 3'),('Name 4', 'Name 4')]
    )
    departmentLocation =  models.CharField(
        max_length=100,
        choices=[('Location 1', 'Location 1'),('Location 2', 'Location 2'),('Location 3', 'Location 3'),('Location 4', 'Location 4')]
    )
    
    def __str__(self):
        return self.user.username