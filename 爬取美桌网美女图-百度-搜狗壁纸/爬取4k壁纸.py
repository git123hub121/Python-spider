import requests
from lxml import etree
from urllib import request
import os
img = []
count = 0
# 不存在文件夹，就创建
if not os.path.exists('4k-wallpaper'):
    os.mkdir('4k-wallpaper')

#该网站为响应式网站，比较灵活，但页面   page =1,2,3,4...的规律
#先爬取一页
print()
scan = input("请输入要爬去的页数：")
for i in range(1,int(scan)+1):
    url = f"http://wallhaven.cc/search?q=id%3A65348&page={i}"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 Edg/86.0.622.63"
    }
    req = requests.get(url,headers=headers)
    #print(req.status_code)
    html = etree.HTML(req.text)
    src = html.xpath('//div[@class="thumbs-container thumb-listing infinite-scroll"]/section/ul/li/figure/img/@data-src')
    #print(src)
    img.extend(src)
    #'//div[@class="thumbs-container thumb-listing infinite-scroll"]/section/ul/li/figure/img/@data-src'
    # 图片使用二进制    这一步是保存图片的关键！
    #print(img) 输出不了二进制。因为操作无法执行可视化
      
#print(img)
# for i in img:
#     count += 1
#     print(f'成功下载图片：{i}',count)
#     filename = str(count)+".jpg"
#     request.urlretrieve(i, filename=filename) 有问题，换一种下载方法！
for i in img:
    count += 1
    filename = str(count)+".jpg"
    img_src = requests.get(i,headers=headers).content
    with open(r'./4k-wallpaper/{}'.format(filename), 'wb') as f:
        f.write(img_src)
        print(f'成功下载图片：{filename}',count) 
    
print('=================== 图片全部下载成功啦！ =====================')


#单独使用user-agent被限制爬虫，urllib.error.HTTPError: HTTP Error 403: Forbidden

#下载成功，但是下载的图片不是4k，而是缩略图，审题不清