from typing import List, AsyncIterator
from urllib.request import urlopen
import asyncio

async def fetch(urls: List[str]) -> AsyncIterator[bytes]:
    for url in urls:
        with urlopen(url) as u:
            yield u.read()

async def sizeof(urls: List[str]) -> List[int]:
    return [len(content) async for content in fetch(urls)]

urls = [
    'http://openhome.cc/Gossip/Encoding/',
    'http://openhome.cc/Gossip/Scala/',
    'http://openhome.cc/Gossip/JavaScript/',
    'http://openhome.cc/Gossip/Python/'
]

loop = asyncio.get_event_loop()
sizes = loop.run_until_complete(sizeof(urls))
print(sizes)
