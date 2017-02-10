from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class MyUser(AbstractUser):
	phone=models.CharField(max_length=10,null=True)
	adhaar_card = models.BigIntegerField(unique=True,default=1)
	profile_pic=models.ImageField(upload_to='profile_pics/',null=True,blank=True)
	blood_group = models.CharField(max_length=3,null = True,blank = True)

