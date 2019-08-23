import requests
from bs4 import BeautifulSoup

data = {
    'commit': 'Sign in',
    'login': 'ayscoopy',
    'password': 'ayscgcgg'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}

with requests.Session() as r:
    url = 'https://github.com/session'
    g = r.get(url, headers=headers)
    stew = BeautifulSoup(g.content,  'html.parser')
    data['authenticity_token'] = stew.find('input', attrs={'name': 'authenticity_token'})['value']
    logs = r.post(url , headers=headers, data=data)
    f = open('test.html', 'w')
    f.write(str(logs.content))
    f.close()
    