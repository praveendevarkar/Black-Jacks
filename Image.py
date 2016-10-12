from bs4 import BeautifulSoup
import requests
import os

html = requests.get ("http://www.fernandesjoshua.com/")

soup = BeautifulSoup(html.content, 'html.parser')
imgs = soup.find_all("img",{"alt":True, "src":True})

for img in imgs:
	print (img['src'])