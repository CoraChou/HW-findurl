import json
import urllib.request as req
import bs4
def getdata (url) :
     #url="http://example.com/"
     with req.urlopen(url) as response:
          data=response.read().decode("utf-8")
     from bs4 import BeautifulSoup
     import bs4
     root=bs4.BeautifulSoup(data, "html.parser")
     findurl=root.findAll("a") #用"li"下面print 不能跑,使用"a"可以但會搜到class
     #url=findurl.a["href"]
     for nextlink in findurl:
          print(nextlink["href"])#問老師為什麼要用[] , 我要的是尋找href標籤
          
     return(nextlink)

#主程序 抓取多個頁面
urls="https://www.iana.org"
urls= (getdata(urls)) #拿到第二層的url
print(urls)

##拿到第三層的url
count = 0
while count < 2:
     urls= (getdata(urls))
     if urls[0] != "h":
          urls = "https://www.iana.org"+urls
          count += 1
          print(urls)