import requests
from bs4 import BeautifulSoup
import json

article_list = []


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
        if '刪除' not in title:
            link = 'https://www.ptt.cc' + \
                art.find('div', class_='title').a['href'].strip()
        author = art.find('div', class_='author').getText().strip()
        print(f'title: {title}\nlink: {link}\nauthor: {author}')
        article = {
            'title':title,
            'link':link,
            'author':author
        }
        article_list.append(article)

    next_url = 'https://www.ptt.cc/' + soup.select('#action-bar-container > div > div.btn-group.btn-group-paging > a:nth-child(2)')[0]['href']    
    return(next_url)    


if __name__ == '__main__':
    url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
    for now_page_number in range(10):
        print(f'crawling {url}')
        resp = get_resp(url)
        if resp != 'error':
            url = get_arts(resp)
        print(f'====={now_page_number + 1}/10=====')
    print(article_list)

    with open('ppt-articles.json','w', encoding='utf-8') as f:
        json.dump(article_list,f,ensure_ascii=False,indent=2,sort_keys=True)


