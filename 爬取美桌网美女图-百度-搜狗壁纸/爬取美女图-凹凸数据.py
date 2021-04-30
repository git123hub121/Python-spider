# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 19:15:04 2020
微信公众号: 凹凸数据
@File    ：spider.py
@Author  ：叶庭云
@CSDN    ：https://yetingyun.blog.csdn.net/
"""
import requests
from random import choice, randint
from lxml import etree
import os
from concurrent.futures import ThreadPoolExecutor
from time import sleep


# 自己构造请求头池  用于切换
user_agent = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]

# 不存在文件夹  就创建
if not os.path.exists('女神套图'):
    os.mkdir('女神套图')


# 获取5页的套图的URL
def get_taotu_url():
    taotu_urls = []
    for i in range(1, 6):
        url = f'http://www.win4000.com/meinvtag4_{i}.html'
        headers = {
            'User-Agent': choice(user_agent)
        }
        # 发送请求  获取响应
        rep = requests.get(url, headers=headers)
        # print(rep.status_code)    状态码  200
        # print(rep.text)
        html = etree.HTML(rep.text)
        taotu_url = html.xpath('//div[@class="tab_tj"]/div/div/ul/li/a/@href')
        # 过滤掉无效的url
        taotu_url = [item for item in taotu_url if len(item) == 39]
        # 一个页面有24个图片
        # print(taotu_url, len(taotu_url), sep='\n')
        taotu_urls.extend(taotu_url)

    return taotu_urls


# 进入套图详情页爬取图片
def get_img(url):
    #print(url)
    headers = {
        'User-Agent': choice(user_agent)
    }
    # 发送请求  获取响应
    rep = requests.get(url, headers=headers)
    # 解析响应
    html = etree.HTML(rep.text)
    # 获取套图名称   最大页数
    name = html.xpath('//div[@class="ptitle"]/h1/text()')[0]
    os.mkdir(r'./女神套图/{}'.format(name))
    max_page = html.xpath('//div[@class="ptitle"]/em/text()')
    # 字符串替换  便于之后构造url请求
    url1 = url.replace('.html', '_{}.html')
    # 翻页爬取这组套图的图片
    for i in range(1, int(max_page[0]) + 1):
        # 构造url
        url2 = url1.format(i)
        # 休眠 
        sleep(randint(1, 3))
        # 发送请求  获取响应
        reps = requests.get(url2, headers=headers)
        # 解析响应
        dom = etree.HTML(reps.text)
        # 定位提取图片下载链接
        src = dom.xpath('//div[@class="main-wrap"]/div[1]/a/img/@data-original')[0]
        # 构造图片保存的名称
        file_name = name + f'第{i}张.jpg'
        # 请求下载图片  保存图片  输出提示信息
        img = requests.get(src, headers=headers).content
        with open(r'./女神套图/{}/{}'.format(name, file_name), 'wb') as f:
            f.write(img)
            print(f'成功下载图片：{file_name}')


# 主函数调用  开多线程
def main():
    taotu_urls = get_taotu_url()
    with ThreadPoolExecutor(max_workers=4) as exector:
        exector.map(get_img, taotu_urls)
    print('=================== 图片全部下载成功啦！ =====================')
    
    
if __name__ == '__main__':
    main()
