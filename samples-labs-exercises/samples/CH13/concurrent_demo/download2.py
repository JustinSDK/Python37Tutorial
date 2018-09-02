from concurrent.futures import ThreadPoolExecutor, Future
from urllib.request import urlopen

def readUrlAsync(url: str, executor: ThreadPoolExecutor) -> Future:
    def _readUrl():
        with urlopen(url) as u:
            return u.read()

    return executor.submit(_readUrl)

def download(url: str, filename: str, executor: ThreadPoolExecutor):
    def save(content):
        with open(filename, 'wb') as f:
            f.write(content)

    readUrlAsync(url, executor).add_done_callback(lambda future: save(future.result()))

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
        download(url, filename, executor)

