from urllib.parse import urlencode
from urllib.request import urlopen
import json
import os
import datetime

def download(date: str, file: str):
    params = urlencode({'response': 'json', 'date': date})
    url = f'http://www.twse.com.tw/indicesReport/MI_5MINS_HIST?{params}'
    with urlopen(url) as resp, open(file, 'w', encoding='UTF-8') as f:
        f.write(resp.read().decode('UTF-8'))

def load(file: str):
    with open(file, 'r', encoding='UTF-8') as f:
        return json.load(f)

def show(history: dict):
    print(history['title'], end='\n\n')
    for field in history['fields']:
        print(f'{field:<8}\t', end='')

    print()
    for d in history['data']:
        print('\t'.join(d))


year = input('西元：')
month = input('月份：')
date = f'{year}{month:0>2}01'
file = f'{date}.json'
today = datetime.date.today()

if not os.path.exists(file) or (today.year == int(year) and today.month == int(month)):
    download(date, file)

show(load(file))