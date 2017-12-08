from six.moves import urllib
import re,os,win32api,win32gui
from win32api import *
from win32gui import *
import win32con
import sys
import struct
import time
import json



pic_dir="E:/Picture/bingPicture"
# pic_dir="E:"
bing_rul="http://bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&nc=1439260838289&pid=hp&video=1"
times=10
waitSeconds=15
isConnected=False
try:
    urllib.request.urlopen("http://www.baidu.com")
    isConnected=True
except:
    isConnected=False
while not isConnected:
    i=i+1
    print("can't connect internet,has been test--",i,"--th")
    time.sleep(waitSeconds)
    try:
        urllib.request.urlopen("http://www.baidu.com")
        isConnected=True
    except:
        isConnected=False
    if i==times:
        print("time has been waste,program will exit")
        exit()
content=urllib.request.urlopen(bing_rul).read().decode('utf-8')
result=json.loads(content)
wallpaper_rul=result['images'][0]['url']
pic_name=wallpaper_rul.split('/')[-1]
if wallpaper_rul.find('http')<0:
    wallpaper_rul="http://www.bing.com"+wallpaper_rul
img_src=urllib.request.urlopen(wallpaper_rul).read()
img_file=pic_dir+'/'+pic_name
if os.path.isfile(img_file):
    print("the file has being")
else:
    print("start download ")
    with open(img_file,'wb') as f:f.write(img_src)

k=win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
win32api.RegSetValueEx(k,"WallpaperStyle",0,win32con.REG_SZ,"0")
win32api.RegSetValueEx(k,"TileWallpaper",0,win32con.REG_SZ,"0")
win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,img_file,1+2)#设置桌面背景



