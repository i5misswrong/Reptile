from bs4 import BeautifulSoup
import urllib,re
url_one={'name': '穿越小说', 'url': 'http://www.jjxsw.com/txt/Chuanyue/'}
# index=10
connet=urllib.request.urlopen(url_one['url']).read().decode('utf-8')
soup=BeautifulSoup(connet)

divs=soup.find_all("div",class_="pager")
for index in range(2,5):
    # print(index)
    for i in divs:
        # print(re.search(str(index),i.find_all('a').string))
        url=i.find_all('a')
        for u in url:
            if u.get_text():

                if (re.match(str(index),u.get_text())):
                    print(u)
            # print(u.get_text())
# print(divs)