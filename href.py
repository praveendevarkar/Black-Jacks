from bs4 import BeautifulSoup
import requests
import os

html = requests.get ("http://www.fernandesjoshua.com/")

soup = BeautifulSoup(html.content, 'html.parser')

for a in soup.find_all('a', href=True):
    print (a['href'])