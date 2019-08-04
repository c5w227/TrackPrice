from django.db import models
from django.core.validators import validate_email

# Create your models here.
class Product(models.Model):
	ID					=	models.AutoField(primary_key=True)
	URL					=	models.TextField(blank=False, null=False)
	Email				=	models.TextField(blank=True,null=True)
	Active				=	models.BooleanField(default=True)
	Price				=	models.IntegerField(blank=False, null=False)
	created_by			=	models.IntegerField(blank=True, null=True)
	created_datetime    =	models.DateTimeField(blank=True, null=True)
	modified_by			=	models.IntegerField(blank=True, null=True)
	modified_datetime	=	models.DateTimeField(blank=True, null=True)
	user_name			=	models.CharField(blank=True, null=True,max_length=120)
 	
