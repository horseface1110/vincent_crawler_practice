import requests

'''
url = 'https://www.google.com'
res = requests.get(url)
print(type(res),res)
'''
'''
url_1 = 'https://www.google.com/search?q=IThome&oq=IThome'
res = requests.get(url_1)
print(res.url,type(res),res)
'''
'''
url_2 = 'https://zh.wikipedia.org/'
data = {'account':'testOwO','password':'testOwO'}
print(requests.post(url_2,data=data).json)
'''
'''
# request header
url = 'https://snake-game-backend.herokuapp.com/Alldatas'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
headers = {
    'User_agent' : user_agent
}
print(requests.get(url,headers=headers).status_code)
'''
'''
# proxy
看不懂
'''
'''
# cookies
url = 'https://www.facebook.com/'
cookies = {
	'account' : 'testOwO',
	'password' : 'testOwO'
}
print(requests.get(url).status_code)
'''