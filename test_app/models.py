from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
     email=models.EmailField(unique=True, max_length=150)

     USERNAME_FIELD='email'
     REQUIRED_FIELDS=['username']

     def __str__(self) -> str:
           return self.email





class Course(models.Model):
        name=models.CharField(max_length=200)
        

        def __str__(self) -> str:
            return self.names
        


class Student(models.Model):
        names=models.CharField(max_length=200)
        age=models.PositiveIntegerField(default=0)
        email=models.EmailField(max_length=200)
        address=models.TextField()
        courses=models.ForeignKey(Course, on_delete=models.CASCADE, default=1)
        
    

        def __str__(self) -> str:
            return self.names
        


        