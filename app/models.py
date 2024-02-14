from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.



class UserProfile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=100,default=None)
    last_name=models.CharField(max_length=100,default=None)
    image=models.ImageField(upload_to='media/',blank=True)
    
class Catergory(models.Model) :
    name=models.CharField(max_length=100)
    def __str__(self) -> str:
        return f'{self.name}'

class Locations(models.Model):
    location=models.CharField(max_length=225)
    def __str__(self) -> str:
        return f'{self.location}'
        

class ServiceProvider(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    Category=models.ForeignKey(Catergory,on_delete=models.CASCADE)
    Shop_name=models.CharField(max_length=100)
    Location=models.ForeignKey(Locations,on_delete=models.CASCADE,default=None)
    Description=models.TextField(blank=True)
    approve = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.Shop_name}' 

class Requests(models.Model):
    User=models.ForeignKey(User, on_delete=models.CASCADE)
    Service = models.ForeignKey(ServiceProvider,on_delete=models.CASCADE)
    datetime = models.DateTimeField(default=timezone.now, blank=True)
    description = models.TextField(blank=True)
    pending = models.BooleanField(default=True)
    accept = models.BooleanField(default=False)
    decline = models.BooleanField(default=False)

    
class Feedback(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    service=models.ForeignKey(ServiceProvider,on_delete=models.CASCADE)
    feedback=models.TextField()
    rating=models.IntegerField(null=False)


