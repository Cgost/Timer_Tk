import requests
import urllib
import time

url = "http://time.artjoey.com/js/basetime.php"
res = requests.get(url)
# res.content type is <byte>
basetime = res.content.decode('ascii')
# var baseTime=1443757229000;
ms = int(basetime.split('=')[1][:-1])   # 用'='分隔, 取出第二組字串的 開頭到倒數第二字元 (最後字元是分號)
sec = ms / 1000       # GMT + 0
twsec = sec+(60*60*8) # GTM + 8

def day_time():
	daysec = twsec % (60 * 60 * 24)   # 僅取出當日開始到目前的秒數
	HH = int(daysec / 60 / 60)
	MM = int(daysec / 60) % 60
	SS = int(daysec % 60)
	return str(HH)+":"+str(MM)+":"+str(SS)

def all_time():
	localtime = time.asctime(time.localtime(sec))
	return str(localtime)

