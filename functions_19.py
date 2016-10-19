from bs4 import BeautifulSoup
import requests


class Functions(object):
    def get_all_links(self, url):
        html = requests.get(url)
        soup = BeautifulSoup(html.content, 'html.parser')
        links = []
        for a in soup.find_all('a', href=True):
            links.append(a['href'])
        return links

    def get_all_images(self, url):
        html = requests.get(url)
        soup = BeautifulSoup(html.content, 'html.parser')
        imgs = soup.find_all("img", {"alt": True, "src": True})
        images = []
        for img in imgs:
            images.append(img['src'])
        return images

    def get_all_text_under_list(self, url):
        html = requests.get(url)
        soup = BeautifulSoup(html.content, 'html.parser')
        list = []
        for lis in soup.find_all('li'):
            list.append(lis.get_text())
        return list

    def get_data_under_class(self, url):
        html = requests.get(url)
        soup = BeautifulSoup(html.content, 'html.parser')
        class_data = []
        for hit in soup.findAll(attrs={'class': 'container'}):
            class_data.append(hit.text)
        return class_data

