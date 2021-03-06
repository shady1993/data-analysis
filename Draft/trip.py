import requests
from bs4 import BeautifulSoup
import re
import numpy as np
import pandas as pd

url = 'https://www.tripadvisor.in/Hotels-g297667-Jaisalmer_Jaisalmer_District_Rajasthan-Hotels.html'
resp = requests.get(url)
html = resp.text
soup = BeautifulSoup(html,'lxml')
#print soup

hotel_name = [app.contents[0] for app in soup.select('a.property_title')]
review_count = [app.contents[0].split()[0] for app in soup.select('a.review_count')]
rating = [app for app in soup.select('span.ui_bubble_rating')]
rank = [rank.contents[0].split()[0] for rank in  soup.select('div.popindex')]
hotel_link = [app['href'] for app in soup.select('a.property_title')]
hotel_facilities = []
for ul_tag in soup.select('ul.icons_list'):
	facility = []
	for li_tag in ul_tag.find_all('li',{'class' : 'hotel_icon'}):
		for div_tag in li_tag.find('div',{'class':'label'}):
			facility.append(div_tag)
	hotel_facilities.append(facility)

#print review_count
#print hotel_name
#print rating
#print hotel_facilities
#print hotel_link
url2 = 'https://www.tripadvisor.in' + hotel_link[0]
response = requests.get(url2)
soup2 = BeautifulSoup(response.text,'lxml')
#print soup2

review_header = [app.text for app in soup2.select('span.noQuotes')]
reviews = [app.text for app in soup2.select('p.partial_entry')]
#print reviews