from urllib import request  #从urllib库里导入request模块
from bs4 import BeautifulSoup   #从BeautifulSoup4(bs4)库里导入BeautifulSoup模块
import re   #导入正则表达式模块re模块
import time     #导入time模块
url = "https://www.zhihu.com/question/64252714"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
page = request.Request(url, headers=headers)
html = request.urlopen(url).read().decode('utf-8')
# print(html)
soup = BeautifulSoup(html, 'html.parser')

#class
data = []
imgurls = soup.find_all("img",class_="origin_image zh-lightbox-thumb lazy")
for imgurl in imgurls:
    imgurl = str(imgurl).strip()
    links = re.findall(r'data-original="(.*?)?source=1940ef5c"',imgurl)[0].replace('?',"")
    data.append(links)
#links = soup.find_all('img', class_="origin_image zh-lightbox-thumb lazy", src = re.compile(r'data-original="(.*?)?source=1940ef5c"'))   #$	匹配字符串的末尾
# print(data)

path = r'C:\Users\Administrator\Pictures\Python图片\知乎图片'  #保存到某个文件夹下
for link in data:
    print(link)
    # request.urlretrieve(link, path + '\%s.jpg' % time.time())
#运行结果
#读取图片并将其下载到本地文件夹
#由于知乎修改了代码，我们这里需要对其转变一种方式

