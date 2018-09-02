from typing import BinaryIO
import urllib.request

def dump(src: BinaryIO, dest: BinaryIO):
    with src, dest:
        dest.write(src.read())

dump(
    urllib.request.urlopen('http://openhome.cc'),
    open('index.html', 'wb')
)