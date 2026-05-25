from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=25)
    password = models.CharField(max_length=20)
    age = models.CharField(max_length=5)
    companyName = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name
    


class userModel(models.Model):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    mobile = models.CharField(max_length=12)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    

