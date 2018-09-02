from urllib.request import urlopen
import asyncio

async def load_url(url: str) -> bytes:
    with urlopen(url) as u:
        return u.read()

async def save(filename: str, content: bytes):
    with open(filename, 'wb') as f:
        f.write(content)

async def download(url: str, filename: str):
    content = await load_url(url)
    await save(filename, content)

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