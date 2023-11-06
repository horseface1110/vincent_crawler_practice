import re
import requests
from bs4 import BeautifulSoup

dollers = input('請輸入要查詢的貨幣：')

url = f'https://www.google.com/search?q={dollers}'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
resp = requests.get(url, headers={
    'user-agent':user_agent
})

soup = BeautifulSoup(resp.text,'html5lib')
ele = soup.find('span',class_ = 'DFlfde SwHCTb')

if ele:
    print(f'目前1{dollers}為{ele.text}元')
else:
    print("目前沒有匯率")