#-*-coding:utf-8-*-
# 2017.1.5 18:00 yantai
# 抓取烟大计算机学院老师的资料
from __future__ import unicode_literals 
import requests
from bs4 import BeautifulSoup
home='http://computer.ytu.edu.cn/news/?c=teacher&a=teacherlist'#首页地址
def page_loop(page=1):
	res = requests.get(home+'&page='+str(page))#切换页面功能为自己开发！顿时脑洞大开
	res.encoding='utf-8'
	soup=BeautifulSoup(res.text,'html.parser')
	for teacher in soup.select('.lead_1'):
		name=teacher.select('.lea_name')[0].text
		js=teacher.select('.lea_js')[0]
		call=js.select('.call')[0].text
		print name,call
	page = int(page) + 1
	if(page>8):
		exit()#到达尾页则停止
	else:
		print u'开始抓取下一页'
		print 'the %s page' % page
		page_loop(page)
#----------------------------------------------
page_loop()#执行爬虫程序
	
		