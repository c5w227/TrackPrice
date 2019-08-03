from django.contrib import admin
import datetime

# Register your models here.
from .models import Product



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	exclude = ['created_by','modified_by','created_datetime','modified_datetime','user_name']
	def save_model(self, request, obj, form, change):
		if not obj.pk:
			obj.created_by			=	request.user.id
			obj.created_datetime	=	datetime.datetime.now()
			if request.user.first_name !="" and request.user.last_name !="":
				obj.user_name		=	request.user.first_name+" "+request.user.last_name
			else:
				obj.user_name		=	request.user.username
			if 	obj.Email == "" or obj.Email is None:
				obj.Email			=	request.user.email	 
			super().save_model(request, obj, form, change)
		if change:
			obj.modified_by				=	request.user.id
			obj.modified_datetime		=	datetime.datetime.now()
			if request.user.first_name !="" and request.user.last_name !="":
				obj.user_name		=	request.user.first_name+" "+request.user.last_name
			else:
				obj.user_name			=	request.user.username
			if 	obj.Email == "" or obj.Email is None:
				obj.Email			=	request.user.email
			super().save_model(request, obj, form, change)
