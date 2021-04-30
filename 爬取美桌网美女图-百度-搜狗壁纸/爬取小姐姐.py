import requests
from lxml import etree
import os
import urllib
import urllib.request
#爬虫过程中，一般会使用requests.get()方法获取一个网页上的HTML内容，然后通过lxml库中的etree.HTML来解析这个网页的结构，最后通过xpath获取自己所需的内容
count = 0
for i in range(1,6):
    url = f"http://www.win4000.com/meinvtag4_{i}.html"
    header = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 Edg/86.0.622.63"
    }
    request = requests.get(url,headers=header)
    #print(request.status_code) #测试成功
    #print(request.text) #1 
    html = etree.HTML(request.text)
    #print(html) #输出<Element html at 0x24738c99b08>
    url_img = html.xpath('//div[@class="w1180 clearfix"]/div/div/div[@class="tab_tj"]/div/div/ul/li/a/img/@data-original')
    #print(type(url_img))
    for i in url_img:
        #url_img.append(i)
        count += 1
        print(i,count)
        name = "sexuality"#对于不同图片及时修改name，防止被替换
        filename = "C:\\Users\\Administrator\\Pictures\\Python图片\\meinv\\"+name+str(count)+".jpg"
        urllib.request.urlretrieve(i, filename=filename)
#print(url_img)
