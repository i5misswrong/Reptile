from bs4 import BeautifulSoup
# import urllib,urllib3
from six.moves import urllib
import re
import sys

def getUrl(url):

    pass

nove_down_dir="D:/"
nove_name="test.txt"
novel_01_url="http://www.jjxsw.com/txt/dl-47-26465.html"
txtName="重生之影后的算命群"
src="http://down2.txt99.com/d/file/p/txt/2017/"

dirc=nove_down_dir+"/"+nove_name
content=urllib.request.urlopen(novel_01_url).read().decode('utf-8')
soup=BeautifulSoup(content)
tags=soup.find_all("a")
title=soup.find_all("title")

downString="普通线路"
lo=[]
s=""
for tag in tags:
    a=tag.get('href')
    lo.append(a)
    # a.find(downString)
for l in lo:
    if re.search("http:",l):

        s=urllib.parse.quote(txtName)
        real=src+s+".txt"
        # print(src+s+".txt")
        novel_src=urllib.request.urlopen(real).read()
        # print(novel_src)
        with open(dirc,'wb') as f:f.write(novel_src)

# print(lo)
# print(lo)

