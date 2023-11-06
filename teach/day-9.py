from bs4 import BeautifulSoup
import requests

'''
url = 'https://www.youtube.com/watch?v=rm-0EmdX43c&list=RDMM&index=30'
resp = requests.get(url)

soup = BeautifulSoup(resp.text,'html5lib')

print(soup.title.getText())
'''

url = 'https://www.youtube.com/watch?v=0HTAKT-JIaA&list=RDMM&index=27'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html5lib')

link = soup.find('img')
print(link)

## 這裡瘋狂失敗欸