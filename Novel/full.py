from bs4 import BeautifulSoup
import re,sys,urllib

url_all={'name': '穿越小说', 'url': 'http://www.jjxsw.com/txt/Chuanyue/',
         'name': '重生小说', 'url': 'http://www.jjxsw.com/txt/chongshengxiaoshuo/',
         'name': '历史架空', 'url': 'http://www.jjxsw.com/txt/Lsjs/',
         'name': '总裁豪门', 'url': 'http://www.jjxsw.com/txt/Qinggan/',
         'name': '现代言情', 'url': 'http://www.jjxsw.com/txt/Young/',
         'name': '仙侠', 'url': 'http://www.jjxsw.com/txt/Wuxia/'}
url_one={'name': '穿越小说', 'url': 'http://www.jjxsw.com/txt/Chuanyue/'}
url_01="http://www.jjxsw.com"
urls=[]
content=urllib.request.urlopen(url_one['url']).read().decode('utf-8')
soup=BeautifulSoup(content)
divs=soup.find_all("div",class_="listbg")


for i in divs:

    # print(i.a['href'])
    urls.append(url_01+i.a['href'])
print(urls)
    # print("----------------------------")

        # if re.search("txt",i['href']):
        #     print(i)
    # print(i)
# print(soup)