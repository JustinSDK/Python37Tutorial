from urllib.request import urlopen
import asyncio

async def download(url: str, file: str):
    with urlopen(url) as u, open(file, 'wb') as f:
        f.write(u.read())

urls = [
    'http://openhome.cc/Gossip/Encoding/',
    'http://openhome.cc/Gossip/Scala/',
    'http://openhome.cc/Gossip/JavaScript/',
    'http://openhome.cc/Gossip/Python/'
]

filenames = [
    'Encoding.html',
    'Scala.html',
    'JavaScript.html',
    'Python.html'
]

loop = asyncio.get_event_loop()
tasks = [loop.create_task(download(url, filename))
         for url, filename in zip(urls, filenames)]
loop.run_until_complete(asyncio.wait(tasks))