from django.db import models
from accounts.models import MyUser
# Create your models here.
class History(models.Model):
	history_pic=models.ImageField(upload_to='history_pics/',null=True,blank=True)
	user=models.ForeignKey(MyUser)
	time=models.DateTimeField(auto_now=False,auto_now_add=True)
	image_title=models.CharField(max_length=120,null=True,blank=True)
	Disease=models.CharField(max_length=120)
	blood_sugar_level=models.CharField(max_length=20,null=True,blank=True)
