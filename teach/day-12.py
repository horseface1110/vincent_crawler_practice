import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
def get_resp(url):
    cookies = {
        'over18':'1'
    }
    resp = requests.get(url,cookies=cookies)
    if resp.status_code != 200:
        return 'error status code'
    else:
        return resp


def get_arts(resp):
    soup = BeautifulSoup(resp.text,'html5lib')
    arts = soup.find_all('div',class_='r-ent')

    for art in arts:
        title = art.find('div', class_='title').getText().strip()
        if not title.startswith('(本文已被刪除)'):
            link = 'https://www.ptt.cc' + \
                art.find('div', class_='title').a['href'].strip()
        author = art.find('div', class_='author').getText().strip()
        print(f'title: {title}\nlink: {link}\nauthor: {author}')
    next_url = 'https://www.ptt.cc/' + soup.select('#action-bar-container > div > div.btn-group.btn-group-paging > a:nth-child(2)')[0]['href']
    return(next_url)    

for i in range(10):
    resp = get_resp(url)
    url = get_arts(resp)

