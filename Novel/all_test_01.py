from bs4 import BeautifulSoup
import re,sys,urllib
jiujiu_url="http://www.jjxsw.com/"
novel_type={"chuanyue":"http://www.jjxsw.com/txt/Chuanyue/",
            "chongsheng":"http://www.jjxsw.com/txt/Chuanyue/"}

def get_paging(noveltype):
    index=1
    paging_numbe=3
    paging = []
    paging.append(noveltype)
    for n in range(paging_numbe):
        if index==1:
            url_paging=noveltype
        else:
            url_paging=paging[index-2]
        content_01 = urllib.request.urlopen(url_paging).read().decode('utf-8')
        soup_01 = BeautifulSoup(content_01, "lxml")
        divs_01 = soup_01.find_all("div", class_="pager")
        for i in divs_01:
            url=i.find_all('a')
            for u in url:
                if u.get_text():
                    if re.match("下一页",u.get_text()):
                        paging.append(jiujiu_url+u['href'])
                        # print(jiujiu_url+u['href'])
        index = index + 1
    # for i in paging:
    #     print(i)
    return paging
def get_detail(paging=[]):
    for p in paging:
        urls = []
        all_mes = []
        indexs = 1

        content = urllib.request.urlopen(p).read().decode('utf-8')
        soup = BeautifulSoup(content, "lxml")
        divs = soup.find_all("div", class_="listbg")

        for i in divs:
            # print(i.a['href'])
            urls.append(jiujiu_url + i.a['href'])
        # print(urls)
        for i in urls:
            book_mes = {"name": "",  # 书名
                        "url_0": "http://www.jjxsw.com",  # 首页
                        "url_1": "http://www.jjxsw.com/txt/Chuanyue/index_2.html",  # 分类页
                        "url_2": "",  # 详情页
                        "url_3": "",  # 下载页
                        "url_4": ""}  # 真实下载链接
            book_mes["url_2"] = i
            cont_01 = urllib.request.urlopen(i).read().decode('utf-8')
            soup_01 = BeautifulSoup(cont_01, "lxml")
            divs_01 = soup_01.find_all("div", class_="listbg")
            book_names = soup_01.h1
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
            soup02 = BeautifulSoup(cont_02, "lxml")
            book_url_02 = soup02.find_all("a")
            s = "http://"
            for i in book_url_02:
                if re.search(s, i['href']):
                    book_mes["url_4"] = i['href']
            all_mes.append(book_mes)
        for i in all_mes:
            print(i)


paging=get_paging(novel_type["chuanyue"])
get_detail(paging)

# print(paging)