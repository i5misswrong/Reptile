import re,sys,urllib
from bs4 import BeautifulSoup

book_mes={"name":"良田美锦",#书名
          "url_0":"http://www.jjxsw.com",#首页
          "url_1":"", #分类页
          "url_2":"http://www.jjxsw.com/txt/26490.htm",#详情页
          "url_3":"",#下载页
          "url_4":""}#真实下载链接


#--------------get book name----------------------
content01=urllib.request.urlopen(book_mes["url_2"]).read().decode('utf-8')
soup01=BeautifulSoup(content01)
book_names=soup01.h1
for i in book_names:
    bookname=i
bookname=re.sub(('《'),"",bookname)
bookname=re.sub(('》'),"",bookname)
book_mes["name"]=bookname
#------------get url_3 the download page---------
book_url_01=soup01.find_all("a")
for i in book_url_01:
    if i.span:
        book_mes["url_3"]=book_mes["url_0"]+i['href']

#---------get url_4 the download really url-------

content02=urllib.request.urlopen(book_mes["url_3"]).read().decode('utf-8')
soup02=BeautifulSoup(content02)
book_url_02=soup02.find_all("a")
s="http://"
for i in book_url_02:
    if re.search(s,i['href']):
        book_mes["url_4"]=i['href']
print(book_mes)


