from django.db import connection
from products.models import Product
import requests
from bs4 import BeautifulSoup
import re
import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import *

def run():
	product_list		=	Product.objects.filter(Active=1).all()
	for product in product_list:
		URL				=				product.URL.strip()
		name			=				product.user_name.strip()
		email			=				product.Email.strip()
		required_price	=				float(product.Price)
		if(check_price(URL,required_price)):
			if(send_mail(email,URL,name,required_price)):
				product.Active = 0
				product.save()
				print(email)



def check_price(URL,required_price):
	headers		=	{"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"}
	page 		=	requests.get(URL,headers=headers)
	soup 		=	BeautifulSoup(page.content, 'html.parser')

	# amazon have two tag for price either priceblock_ourprice or priceblock_dealprice
	ourprice	=	soup.find(id="priceblock_ourprice")
	dealprice 	=	soup.find(id="priceblock_dealprice")
	global title
	title		=	soup.find(id="productTitle")
	if title is not None:
		title 	= 	title.get_text().strip()

	if ourprice is not None:
		actual_price	=	ourprice.get_text()
	elif dealprice is not None:
		actual_price	=	dealprice.get_text()
	else:
		return False

	if actual_price is not None:
		actual_price	=	re.findall(r"[-+]?\d*\.\d+|\d+", actual_price)
		global float_price
		float_price		=	''
		for price in actual_price:
			float_price +=  price
		float_price		=	float(float_price)	
		if(float_price <= required_price):
			return True
		else:
			return False

def send_mail(email,URL,name,required_price):
	body 				= 	"""\
							<html>
						  		<body>
						    		<p><b>Hi, """+name+"""</b><br><br>
						       			Your product have discount of """+str(required_price-float_price)+""" <a href="""+URL+""">click here</a> to buy your product @"""+str(float_price)+""" 
						    		</p>
						  		</body>
							</html>
							"""
	msg 				= 	MIMEText(body,"html")
	msg['To'] 			= 	formataddr(('Recipient', email))
	msg['From'] 		= 	formataddr(('noreply@pricetracker.com', 'author@example.com'))
	msg['Subject'] 		= 	title

	server 				= 	smtplib.SMTP('smtp.gmail.com',587)
	server.starttls()
	server.login('uptechnotricks@gmail.com','duftwvzvejtksznj')

	server.sendmail(msg['From'], [email], msg.as_string())
	return True
