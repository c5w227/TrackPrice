import requests
from bs4 import BeautifulSoup
import re
import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import *

title = ''
def run():
	URL 				= 	'https://www.amazon.in/Samsung-Galaxy-Storage-Additional-Exchange/dp/B07KXBMYCW/ref=gbph_rlm_s-3_45c6_c9cdc4a1?smid=A14CZOWI0VEHLG&pf_rd_p=1ebe63e0-af55-45f8-88e2-7c1c868945c6&pf_rd_s=slot-3&pf_rd_t=701&pf_rd_i=gb_main&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_r=ZH0F242N8KYQ5YZPAD3W'
	URL					=	URL.strip()
	required_price		=	float(19000)
	if(check_price(URL,required_price)):
		email			=	'jaydhanani36.jd@gmail.com'
		email			=	email.strip()
		name			=	'Jay Dhanani'
		name			=	name.strip()
		send_mail(email,URL,name,required_price)

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
	body = """\
				<html>
				  <body>
				    <p><b>Hi, """+name+"""</b><br><br>
				       Your product have discount of """+str(required_price-float_price)+""" <a href="""+URL+""">click here</a> to buy your product @"""+str(float_price)+""" 
				    </p>
				  </body>
				</html>
				"""
	msg = MIMEText(body,"html")
	msg['To'] = formataddr(('Recipient', 'jaydhanani36@yahoo.com'))
	msg['From'] = formataddr(('noreply@pricetracker.com', 'author@example.com'))
	msg['Subject'] = title

	server = smtplib.SMTP('smtp.gmail.com',587)
	server.starttls()
	server.login('jaydhanani36.jd@gmail.com','epytrrlhlviewrzc')

	server.sendmail(msg['From'], ['jaydhanani36@yahoo.com'], msg.as_string())