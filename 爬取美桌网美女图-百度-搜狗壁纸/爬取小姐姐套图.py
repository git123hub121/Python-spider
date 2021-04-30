import requests
from lxml import etree
import os
from concurrent.futures import ThreadPoolExecutor
from time import sleep
from random import randint

# 不存在文件夹，就创建
if not os.path.exists('goddess-img'):
    os.mkdir('goddess-img')
# 获取5页的套图URL   以后要学会用函数写！


def get_url():
    # 这个网址只有5页
    taotu_urls = []
    for i in range(1,6):
        url = 'http://www.win4000.com/meinvtag4_{}.html'.format(i)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 Edg/86.0.622.63"
        }
        request = requests.get(url, headers=headers)
        # print(request.status_code)
        # print(request.text)
        html = etree.HTML(request.text)
        taotu_url = html.xpath(
            '//div[@class="w1180 clearfix"]/div/div/div[@class="tab_tj"]/div/div/ul/li/a/@href')
        #taotu_url = [item for item in taotu_url if len(item) == 39]
        # print(type(taotu_url))#这里是列表   <class 'list'>
        # print(taotu_url,len(taotu_url),sep="\n")
        taotu_urls.extend(taotu_url)#只会追加列表的元素 用新列表扩展原来的列表 这一步很关键，我也在思考为什么
    return taotu_urls

# 进入套图详情页爬取图片


def get_img(url):#这里url，就只是需要一个参数而已
    # print(taotu_url)#单独的元素在列表中是str   可测试print(type(taotu_url))
    #print(url)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 Edg/86.0.622.63"
    }
    request = requests.get(url, headers=headers)
    html = etree.HTML(request.text)
    name = html.xpath('//div[@class="ptitle"]/h1/text()')[0]
    os.mkdir(r'./goddess-img/{}'.format(name))
    max_page = html.xpath('//div[@class="ptitle"]/em/text()')
    #print(max_page)
    # 我们爬取的页面是http://www.win4000.com/meinv217803.html<=>http://www.win4000.com/meinv217803_1.html
    # 其余都是—_2,_3...所以需要字符串替换，构建一个内循环
    # 字符串替换  便于之后构造url请求   str.replace(old, new[, max])
    url = url.replace('.html', '_{}.html')
    # 翻页爬取这组套图的图片
    for i in range(1, int(max_page[0])+1):
        new_url = url.format(i)  # 构造url
        # 休眠
        sleep(randint(1, 3))
        # 重新发送新的请求  获取响应
        request = requests.get(new_url, headers=headers)
        new_html = etree.HTML(request.text)
        # 定位提取图片下载链接
        src_img = new_html.xpath('//div[@class="main-wrap"]/div[1]/a/img/@data-original')[0]
        print(src_img)#测试
        # 构造图片保存的名称
        file_name = name + f'第{i}张.jpg'
        # 请求下载图片  保存图片  输出提示信息
        img = requests.get(src_img, headers=headers).content    # 图片使用二进制    这一步是保存图片的关键！
        #print(img) 输出不了二进制。因为操作无法执行可视化
        with open(r'./goddess-img/{}/{}'.format(name, file_name), 'wb') as f:
            f.write(img)
            print(f'成功下载图片：{file_name}')


def main():
    taotu_urls = get_url()
    with ThreadPoolExecutor(max_workers=4) as exector:
        exector.map(get_img, taotu_urls)
    print('=================== 图片全部下载成功啦！ =====================')


if __name__ == '__main__':
    main()
