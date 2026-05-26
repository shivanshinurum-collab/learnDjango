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
    


from django.db import models

class UserModel(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=12)

    password = models.CharField(max_length=128)

    avatar_url = models.CharField(max_length=255, null=True, blank=True)

    level = models.CharField(max_length=30, default="beginner")

    total_quizzes = models.IntegerField(default=0)
    wallet_balance = models.IntegerField(default=0)

    rank = models.IntegerField(default=0)
    total_rewards = models.IntegerField(default=0)

    token = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

