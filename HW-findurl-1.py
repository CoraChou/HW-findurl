import json
import urllib.request as req 
import bs4
from urllib.parse import urljoin
 
def getdata(url) :
    with req.urlopen(url) as response:
        data = response.read().decode("utf-8")
    soup = bs4.BeautifulSoup(data, "html.parser")
    a_tags = soup.findAll("a")   
    return a_tags

urlbox = set()

#主程序 
url = input("請輸入網址:") #"http://example.com/"
urlbox.add(url)
urls = getdata(url)

layer = input("請輸入層數(1 or 2):")

if layer == "1" : 
    for a_tag in urls:    
        href_1 = urljoin(url, a_tag["href"])
        urlbox.add(href_1)
elif layer == "2" :
    for a_tag in urls:    
        href_1 = urljoin(url, a_tag["href"])
        urlbox.add(href_1) #拿到第一層
    href_2 = getdata(href_1)
    for a_tag2 in href_2: 
        href_2 = urljoin(href_1, a_tag2["href"])
        urlbox.add(href_2) #拿到第二層
else:
    print("請重新輸入")
    

list = list(urlbox)
count = len(urlbox)
print("網址總數:" , count )
for idx1 , list_url in enumerate (urlbox): #轉成json
    json_url = json.dumps(list_url)
    print(json_url)     