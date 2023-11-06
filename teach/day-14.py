import json
import re  #?
from bs4 import BeautifulSoup
import requests

vers = []

version_list = ['21.04/', '20.10/', '20.04/', '18.04/', '16.04/', '14.04/']   ###這些版本都消失了，所以找不到
url = 'http://ftp.ubuntu-tw.org/ubuntu-releases/'

for version in version_list:
    resp = requests.get(url + version)
    soup = BeautifulSoup(resp.text,'html5lib')

    desktop_iso = soup.find('a', string=re.compile('ubuntu-\d{2}\.\d{2}\.?\d{0,2}-desktop-amd64\.iso'))['href']
    server_iso = soup.find('a',string=re.compile('ubuntu-\d{2}\.\d{2}\.?\d{0,2}(-live)?-server-amd64\.iso'))['href']

    urls = {
        'version':version,
        'destop_iso': desktop_iso,
        'server_iso': server_iso
    }
    vers.append(urls)

with open('iso_url.json','w',encoding='utf-8') as f:
    json.dump(vers,f,ensure_ascii=False,indent=2,sort_keys=True,)
    