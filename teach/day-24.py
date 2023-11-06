import requests
from bs4 import BeautifulSoup
import json



if __name__ == "__main__":
    list = []
    num = int(input('請輸入需要的數量'))
    for i in range(num):
        url = 'https://api.thecatapi.com/v1/images/search'
        resp = requests.get(url)
        json_resp = json.loads(resp.text)
        list.append(json_resp[0]['url'])
    with open('貓貓連結.json','w',encoding='utf-8') as f:
        json.dump(list,f,ensure_ascii=False,indent=2,sort_keys=True)
