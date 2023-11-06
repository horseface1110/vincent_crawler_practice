import requests
from bs4 import BeautifulSoup
import json

url = 'https://hiyokoyarou.com/'
list_url = []
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'

headers = {
    'user_agent':user_agent
}

def list(url):                                                     ## 從list畫面到detial
    resp = requests.get(url,headers=headers)                       ## 要想辦法把整個頁面的url都抓起來
    soup = BeautifulSoup(resp.text,'html5lib')
    # 找到目標元素
    arts = soup.find('div',class_ = 'l-main__body p-front')
    links = arts.find_all('a')

    hrefs = [link['href'] for link in links]
    print(hrefs)



























def detial(url):
    resp = requests.get(url,headers=headers)
    soup = BeautifulSoup(resp.text,'html5lib')
    # 找到目標元素
    links = soup.select('#main_content > div > ul > li:nth-child(1)')

    # 提取 href 屬性值
    hrefs = [link['href'] for link in links]

    # 輸出結果
    print(links)

def next_page(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text,'html5lib')
    next_page_url = soup.select('#main_content > div > nav > a.next.page-numbers')[0]['href']
    return next_page_url


if __name__ == '__main__':
    list(url)
