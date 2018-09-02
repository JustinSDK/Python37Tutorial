from typing import Callable
from concurrent.futures import ThreadPoolExecutor
from urllib.request import urlopen

Consume = Callable[[bytes], None]

def load_url(url: str, consume: Consume):
    with urlopen(url) as u:
        consume(u.read())

def save(filename: str) -> Consume:
    def _save(content):
        with open(filename, 'wb') as f:
            f.write(content)
    return _save

with ThreadPoolExecutor() as executor:
    url = 'https://openhome.cc/Gossip/Python/'
    loaded_callback = save('Python.html')
    executor.submit(load_url, url, loaded_callback)



