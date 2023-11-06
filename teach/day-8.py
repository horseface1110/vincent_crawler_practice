from requests_html import HTMLSession

'''
session = HTMLSession()

r = session.get('https://ithelp.ithome.com.tw/users/20134430/ironman/4307')
print(type(r.html))
'''
'''
# 資料過濾
session = HTMLSession()

r = session.get('https://ithelp.ithome.com.tw/users/20134430/ironman/4307')

#print(r.text)   #網頁原始碼
#print(r.url)     #網頁網址
#print(r.links)    #網頁內其他網址
#print(r.html.text) #除去html
'''
'''
# CSS 選擇器  使用>

session = HTMLSession()
r = session.get('https://ithelp.ithome.com.tw/users/20134430/ironman/4307')

ele = r.html.find('body > div.container.index-top > div > div > div.board.leftside.profile-main > div.ir-profile-content')
print(ele[0].text)
'''
'''
# XPath選擇器 使用/

session = HTMLSession()
r = session.get('https://ithelp.ithome.com.tw/users/20134430/ironman/4307')
ele = r.html.xpath('/html/body/div[2]/div/div/div[2]/div[1]')
print(ele[0].text)
'''
'''
# search、search all
# template 模板，回傳模板{}裡面的字
session = HTMLSession()
r = session.get('https://ithelp.ithome.com.tw/users/20134430/ironman/4307')
ele = r.html.xpath('/html/body/div[2]/div/div/div[2]/div[1]')

print(ele[0].search_all('【Day{}】'))
'''