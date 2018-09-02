import threading
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

for url, filename in zip(urls, filenames):
    t = threading.Thread(target = download, args = (url, filename))
    t.start()


