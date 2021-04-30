#爬取博客
import urllib
import json
import requests
from bs4 import BeautifulSoup

# url = "https://pic.sogou.com/pics/recommend?category=%E5%A3%81%E7%BA%B8"    
#   https://image.baidu.com/
# res = requests.get(url)
# soup = BeautifulSoup(res.text,'html.parser')
#print(soup.select('img'))   #理论上获取的是一个列表，但是输出只有一个，这说明图片资料不在该img标签里面，或者说无法通过img标签去获取，因为它是动态加载，要找到ajax

def getSouGou(category,length,path):
    n = length
    cate = category
    imgs = requests.get('https://pic.sogou.com/pics/channel/getAllRecomPicByTag.jsp?category='+cate+'&tag=%E5%85%A8%E9%83%A8&start=0&len='+str(n))
    jd = json.loads(imgs.text)
    jd = jd['all_items']
    imgs_url = []
    for j in jd:
        imgs_url.append(j['pic_url'])#bthumbUrl 修改一下就好了！
    m = 1
    for img in imgs_url:
        print('====='+str(m)+'.jpg'+'正在下载')
        urllib.request.urlretrieve(img,path+str(m)+'.jpg')
        m = m+1
    print("下载完成！")

getSouGou('壁纸',10,r'C:\Users\Administrator\Pictures\Python图片/搜狗壁纸/')

#问题：这下载的是缩略图，并不是我想要的，所以该咋办！
