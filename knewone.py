#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import time

url = 'https://knewone.com/discover?page=3'
def geturl(url,data=None):
	

	
	wb_data = requests.get(url)
	soup = BeautifulSoup(wb_data.text,'lxml')

	titles = soup.select('section.content > h4 > a')
	images = soup.select('a.cover-inner > img')
	links = soup.select('section.content > h4 > a')

	if data == None:
		for title,image,link in zip(titles,images,links):
			data = {
			'title':title.get_text(),
			'image':image.get('src'),
			'link':link.get('href')
			}
			print data

def get_page(start,end):
	for one in range(start,end):
		geturl(url+str(one))
		#time.sleep(2)

get_page(1,10)
