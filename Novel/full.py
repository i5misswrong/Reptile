from bs4 import BeautifulSoup
import re,sys,urllib

url_all={'name': '穿越小说', 'url': 'http://www.jjxsw.com/txt/Chuanyue/',
         'name': '重生小说', 'url': 'http://www.jjxsw.com/txt/chongshengxiaoshuo/',
         'name': '历史架空', 'url': 'http://www.jjxsw.com/txt/Lsjs/',
         'name': '总裁豪门', 'url': 'http://www.jjxsw.com/txt/Qinggan/',
         'name': '现代言情', 'url': 'http://www.jjxsw.com/txt/Young/',
         'name': '仙侠', 'url': 'http://www.jjxsw.com/txt/Wuxia/'}

url_one={'name': '穿越小说', 'url': 'http://www.jjxsw.com/txt/Chuanyue/index_2.html'}
url_01="http://www.jjxsw.com"
urls=[]
all_mes=[]
indexs=1

content=urllib.request.urlopen(url_one['url']).read().decode('utf-8')
soup=BeautifulSoup(content,"lxml")
divs=soup.find_all("div",class_="listbg")

for i in divs:

    # print(i.a['href'])
    urls.append(url_01+i.a['href'])
# print(urls)
for i in urls:
    book_mes = {"name": "",  # 书名
                "url_0": "http://www.jjxsw.com",  # 首页
                "url_1": "http://www.jjxsw.com/txt/Chuanyue/index_2.html",  # 分类页
                "url_2": "",  # 详情页
                "url_3": "",  # 下载页
                "url_4": ""}  # 真实下载链接
    book_mes["url_2"]=i
    cont_01=urllib.request.urlopen(i).read().decode('utf-8')
    soup_01=BeautifulSoup(cont_01,"lxml")
    divs_01=soup_01.find_all("div",class_="listbg")
    book_names=soup_01.h1
    for i in book_names:
        bookname = i
    bookname = re.sub(('《'), "", bookname)
    bookname = re.sub(('》'), "", bookname)
    book_mes["name"] = bookname
    book_url_01 = soup_01.find_all("a")
    for i in book_url_01:
        if i.span:
            book_mes["url_3"] = book_mes["url_0"] + i['href']
    cont_02 = urllib.request.urlopen(book_mes["url_3"]).read().decode('utf-8')
    soup02 = BeautifulSoup(cont_02,"lxml")
    book_url_02 = soup02.find_all("a")
    s = "http://"
    for i in book_url_02:
        if re.search(s, i['href']):
            book_mes["url_4"] = i['href']
    all_mes.append(book_mes)
for i in all_mes:

    print(i)