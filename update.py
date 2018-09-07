import requests
import re

Chapter = []
#获取目录
r = requests.get("http://www.yunxs.com/longzu5/")
Ready = re.compile(r'"\d{7,}.html')
Mulu = Ready.findall(r.text)

#获取每章节url
for i in Mulu:
	i=i.replace('"','')
	Chapter.append("http://www.yunxs.com/longzu5/"+i)

print(len(Chapter))
#查看是否需要更新
filename = 'zhengwen/number.txt'
with open(filename,'r') as file_open:
	a = file_open.read()
	if(int(a)>=len(Chapter)):
		print("没更新呢")
	else:
		i=Chapter[-1]
		j =requests.get(i)
		FilterContent= re.compile(r'&nbsp;.*&nbsp;')
		Content = FilterContent.findall(j.text)
		filename = 'zhengwen/'+'Chapter '+str(int(a))+'.html'
		#写文档
		with open(filename,'w') as file_object:
			file_object.write('<meta charset="UTF-8">')
			file_object.write(Content[0])
			file_object.write('<br /> <a href=\"Chapter '+str(int(a)-1)+'.html\">上一章</a>')	
			file_object.write('&nbsp&nbsp&nbsp&nbsp<a href=\"Chapter '+str(int(a)+1)+'.html\">下一章</a>')			
			with open('zhengwen/list.html','a') as fileList_edit:
				fileList_edit.write("<a href=\"./"+"Chapter "+a+".html\""+"/>"+"Chapter "+a+"</a> <br />") 
		with open('zhengwen/number.txt','w') as file_edit:
			file_edit.write(str(len(Chapter)))
		print('已更新')

