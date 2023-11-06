from bs4 import BeautifulSoup
import requests

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
cookies = {
    'over18':'1'
}
resp = requests.get(url,cookies=cookies)
soup = BeautifulSoup(resp.text,'html5lib')
arts = soup.find_all('div', class_='r-ent')

for art in arts:
    title = art.find('div', class_='title').getText().strip()
    author = art.find('div', class_='author').getText().strip()
    link = 'https://www.ptt.cc' + art.find('div', class_='title').a['href'].strip()
    date = art.find('div',class_ = 'date').getText().strip()
    print(f'title: {title}\nlink:{link}\nauthor:{author}\ndate:{date}')