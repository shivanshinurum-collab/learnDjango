from django.db import models 
from django.core.validators import MinValueValidator , MaxValueValidator

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
    

class quizz(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=50)
    level = models.IntegerField(
        validators=[
        MinValueValidator(1),
        MaxValueValidator(4)
    ])
    op1 = models.CharField(max_length=50)
    op2 = models.CharField(max_length=50)
    op3 = models.CharField(max_length=50)
    op4 = models.CharField(max_length=50)
    ans = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(4)])

    def __str__(self):
        return self.question


class leaderboard(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=25)
    score = models.IntegerField(default=0)
    
    def __str__(self):
        return self.email
    

class userWallet(models.Model):
    email = models.CharField(max_length=25)
    wallet = models.IntegerField()

    def __str__(self):
        return self.email    
