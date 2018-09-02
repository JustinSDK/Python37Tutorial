from typing import Iterator
from urllib.request import urlopen
import re

def save(content: bytes, filename: str):
    with open(filename, 'wb') as dest:
        dest.write(content)

def download(urls: Iterator[str]):
    for url in urls:
        with urlopen(url) as resp:
            content = resp.read()
            filename = url.split('/')[-1]
            save(content, filename)

def download_imgs_from(url: str):
    with urlopen('https://openhome.cc/Gossip') as resp:
        html = resp.read().decode('UTF-8')
        srcs = re.findall(r'(?s)<img.+?src="(.+?)".*?>', html)
        download(f'{url}/{src}' for src in srcs)

download_imgs_from('https://openhome.cc/Gossip')