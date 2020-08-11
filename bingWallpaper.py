import requests, json
import time, os, sys, getpass
import win32api, win32con, win32gui

BASE_URL='https://cn.bing.com'
API='https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN'
CMD = False

def log( msg:str ):
    if(CMD):
        print( msg )
    else:
        with open('D:/Documents/soft/bingWallpaper/bingWallpaper.log', mode='a+') as f:
            data = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            f.write('[ %s ] : %s \n'%(data, msg))
            f.close()
def getFileName()->str:
    name = time.strftime("%Y-%m-%d", time.localtime())
    file_name = 'D:/Pictures/bingWallpaper/' + name + '.png'
    return file_name

def getUrl()->str:
    r = requests.get(API)
    data = json.loads(r.text)
    url = data['images'][0]['url']
    return BASE_URL + url
    
def saveImage(url:str)->str:
    file_name = getFileName()
    log('保存文件路径' + file_name)
    with open(file_name, mode = 'wb') as f:
        data = requests.get(url)
        log('图片下载情况：' + str(data.status_code))
        f.write(data.content)
        f.close()
    return file_name

def setWallPaper(pic:str):
   # open register
   regKey = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
   win32api.RegSetValueEx(regKey,"WallpaperStyle", 0, win32con.REG_SZ, "2")
   win32api.RegSetValueEx(regKey, "TileWallpaper", 0, win32con.REG_SZ, "0")
   # refresh screen
   win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,pic, win32con.SPIF_SENDWININICHANGE)


file_name = getFileName()
if(os.path.exists(file_name)):
    log('今天已经设置过壁纸，跳过设置')
    setWallPaper(file_name)
    exit()
saveImage(getUrl())
setWallPaper(file_name)
