# Python script for Amazon product availability checker
# importing libraries
from lxml import html
import requests
from time import sleep
import time
from excelIO import Input

# Email id for who want to check availability
# receiver_email_id = "EMAIL_ID_OF_USER"
status = []

def check(url):
	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
	
	# adding headers to show that you are
	# a browser who is sending GET request
	page = requests.get(url, headers = headers)
	for i in range(20):
		# because continuous checks in
		# milliseconds or few seconds
		# blocks your request
		sleep(3)
		
		# parsing the html content
		doc = html.fromstring(page.content)
		
		# checking availability
		XPATH_AVAILABILITY = '//div[@id ="availability"]//text()'
		RAw_AVAILABILITY = doc.xpath(XPATH_AVAILABILITY)
		AVAILABILITY = ''.join(RAw_AVAILABILITY).strip() if RAw_AVAILABILITY else None
		return AVAILABILITY


def ReadAsin(id):
	# Asin Id is the product Id which
	# needs to be provided by the user
	Asin = id
	url = "http://www.amazon.in/dp/" + Asin
	print ("Processing: "+url)
	ans = check(url)
	print(ans)
	status.append(ans)

# scheduling same code to run multiple
# times after every 1 minute
def job(id):
	print("Tracking....")
	ReadAsin(id)

# job()
sheet = "data.xlsx"
input = Input(sheet)
products = input.read()
for i in products:
    job(i)

print("\n\n")
for i in status:
	print(i)
input.write(status)

