import requests
from bs4 import BeautifulSoup

url = 'https://humanitec.com/blog'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

links = set()

for link in soup.find_all('a'):
    href = link.get('href')
    if href.startswith('/blog/'):
        url = 'https://humanitec.com' + href
        if url not in links:
            links.add(url)
            print(url)
