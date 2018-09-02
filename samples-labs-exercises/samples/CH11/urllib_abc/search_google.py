from urllib.request import urlopen, Request

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}
request = Request('https://www.google.com.tw/search?q=python', headers=headers)

with urlopen(request) as resp:
    print(resp.read().decode('UTF-8'))