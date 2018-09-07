import requests
import re
from bs4 import BeautifulSoup

Chapter = []
#获取目录
r = requests.get("http://www.yunxs.com/longzu5/")
Ready = re.compile(r'"\d{7,}.html')
Mulu = Ready.findall(r.text)

#获取每章节url
for i in Mulu:
	i=i.replace('"','')
	Chapter.append("http://www.yunxs.com/longzu5/"+i)

#写一个list用于跳转
filename = 'zhengwen/list.html'
with open(filename,'w') as file_write:
	for j in range(1,len(Chapter)):
		file_write.write("<a href=\"./"+"Chapter "+str(j)+".html\""+"/>"+"Chapter "+str(j)+"</a> <br />")

#处理正文
for (z,i) in enumerate(Chapter):
	j =requests.get(i)
	FilterContent= re.compile(r'&nbsp;.*&nbsp;')
	Content = FilterContent.findall(j.text)
	if (Content[0]=='&nbsp;&nbsp;&nbsp;&nbsp;'):   #有一个页面就没有内容
		continue
	filename = 'zhengwen/'+'Chapter '+str(z)+'.html'
	#写文档
	with open(filename,'w') as file_object:
		file_object.write('<meta charset="UTF-8">')
		file_object.write(Content[0])
		file_object.write('<br /> <a href=\"Chapter '+str(z-1)+'.html\">上一章</a>')	
		file_object.write('&nbsp&nbsp&nbsp&nbsp<a href=\"Chapter '+str(z+1)+'.html\">下一章</a>')
with open('zhengwen/number.txt','w') as listedit:
	listedit.write(str(z+1))

'''
#获取每章节标题，获取有问题，作废
ChapterName =[]
a = re.findall('"\d{7,}.html">.*[\u4e00-\u9fa5]',r.text)
for i in a:
	h = re.findall('\u7b2c.*[\u4e00-\u9fa5]',i)
	if (h!=[]):                                #有的爬下来是空的
		ChapterName.append(h[0])
print(ChapterName)
'''
