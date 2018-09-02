import json
from urllib.request import urlopen
from urllib.parse import urlencode

def printVolumeInfo(books: dict):
    for book in books['items']:
        print(book['volumeInfo'])

params = urlencode({'q': 'python'})
url = f'https://www.googleapis.com/books/v1/volumes?{params}'
with urlopen(url) as resp:
    printVolumeInfo(json.loads(resp.read().decode('UTF-8')))

