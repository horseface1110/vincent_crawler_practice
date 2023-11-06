import requests
from bs4 import BeautifulSou
url = 'https://i.ncku.edu.tw/'
#發送 GET 請求到 url，並將回應物件放到 resp
resp = requests.get(url)
# 將 resp.text 也就是 HTML 資料定義到 BeautifulSoup 物件內，並用 html5lib 解析 HTML 內容
soup = BeautifulSoup(resp.text, 'html5lib')

arts = soup.find_all('span', class_='icon_title')

for art in arts:
    link = art.a['href'].strip
    print(f'link:{link}\n')