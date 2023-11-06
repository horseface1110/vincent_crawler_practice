import openpyxl
from bs4 import BeautifulSoup
import requests


def crawler(cointype):
    url = f'https://www.google.com/search?q={cointype}'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    resp = requests.get(url, headers={
        'user-agent':user_agent
    })

    soup = BeautifulSoup(resp.text,'html5lib')
    ele = soup.find('span',class_ = 'DFlfde SwHCTb')

    if ele:
        return(f'{ele.text}')
    else:
        return("目前沒有匯率")
    



workbook = openpyxl.load_workbook('匯率即時更新.xlsx')
sheet = workbook['即時匯率']
mxR = sheet.max_row
cointypes = []
for r in range(2,mxR + 1):
    cointypes.append(sheet[f'A{r}'].value)


now_row = 2
for cointype in cointypes:
    result = crawler(cointype)
    sheet[f'B{now_row}'].value = result
    now_row += 1

workbook.save('匯率即時更新.xlsx')

