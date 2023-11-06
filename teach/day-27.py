import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    resp = requests.get('https://www.dcard.tw/service/api/v2/posts')
    print(resp.text)