from bs4 import BeautifulSoup
import re,sys,urllib


theme=['穿越小说','重生小说','历史架空','总裁豪门','现代言情','仙侠']
mes=[]
url_01="http://www.jjxsw.com"
content=urllib.request.urlopen(url_01).read().decode('utf-8')
soup=BeautifulSoup(content)
url_all=soup.find_all("a")

for i in url_all:
    for t in theme:
        # print(re.search("chuanyue",i['href']))
        # url_class["name"]=i.name
        if i.string:
            if re.search(t,i.string):
                url_class = {"name": "","url": ""}
                url_class["name"]=t
                url_class["url"]=url_01+i['href']
                mes.append(url_class)
print(mes)
