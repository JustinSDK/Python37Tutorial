from urllib.request import urlopen
from bs4 import BeautifulSoup

def save(content, filename):
    with open(filename, 'wb') as dest:
        dest.write(content)

def download(urls):
    for url in urls:
        with urlopen(url) as resp:
            content = resp.read()
            filename = url.split('/')[-1]
            save(content, filename)

def download_imgs_from(url):
    with urlopen('https://openhome.cc/Gossip') as resp:
        soup = BeautifulSoup(resp.read(), 'html.parser')
        srcs = (img.get('src') for img in soup.find_all('img'))
        download(f'{url}/{src}' for src in srcs)

download_imgs_from('https://openhome.cc/Gossip')
