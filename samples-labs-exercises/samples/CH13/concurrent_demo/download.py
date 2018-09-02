from concurrent.futures import ThreadPoolExecutor
from urllib.request import urlopen

def download(url: str, file: str):
    with urlopen(url) as u, open(file, 'wb') as f:
        f.write(u.read())

urls = [
    'https://openhome.cc/Gossip/Encoding/',
    'https://openhome.cc/Gossip/Scala/',
    'https://openhome.cc/Gossip/JavaScript/',
    'https://openhome.cc/Gossip/Python/'
]

filenames = [
    'Encoding.html',
    'Scala.html',
    'JavaScript.html',
    'Python.html'
]

with ThreadPoolExecutor(max_workers=4) as executor:
    for url, filename in zip(urls, filenames):
        executor.submit(download, url, filename)

