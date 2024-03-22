import requests
from bs4 import BeautifulSoup

def get_links(url,base_url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    links = soup.find_all('a')
    L=[]
    for link in links:
        L.append(base_url+link.get('href'))
    return L