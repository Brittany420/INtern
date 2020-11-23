from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractUser, UserManager as AbstractUserManager

class UserManager(AbstractUserManager):
  pass


# Create your models here.
class User(models.Model):
#create student account here !!!!!!!!!!

#    title = models.CharField(max_length=255)

    First_name = models.CharField(max_length=255)
    Last_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255)


 #First_name, Last_name, id, password, username

# class S_info(models.Model):

    major1 = models.CharField(max_length=255)
    major2 = models.CharField(max_length=255)
    career_interest1=models.CharField(max_length=255)
    career_interest2=models.CharField(max_length=255)
    career_interest3=models.CharField(max_length=255)
    level_interest1=models.CharField(max_length=255)
    level_interest2=models.CharField(max_length=255)
    level_interest3=models.CharField(max_length=255)

    skill1=models.CharField(max_length=255)
    skill2=models.CharField(max_length=255)
    skill3=models.CharField(max_length=255)
    skill4=models.CharField(max_length=255)
    skill5=models.CharField(max_length=255)

    availability=models.CharField(max_length=255)
    biography=models.CharField(max_length=255)
    doc1= models.FileField(upload_to='uploads/')
    doc1= models.FileField(upload_to='uploads/')
    doc1= models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.username

class E_account(models.Model):
    employer_name = models.TextField()
    company_name = models.TextField()
    password_1 = models.TextField()
    password_2 = models.TextField()


    #student's student_moreinfo
    #

    #Availability = models.TextField()

    # major
    # career interests
    #
    # career also level of interest
    #
    # technical Skills
    # Availability
    #
    #
    # biography
    #
    # uploaded Documents
