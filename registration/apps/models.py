from django.db import models

# Create your models here.
class Newuser(models.Model):
	UserName= models.CharField(max_length=100)
	Password= models.CharField(max_length=50)
	Email= models.CharField(max_length=50)
	Address= models.CharField(max_length=100)
		
