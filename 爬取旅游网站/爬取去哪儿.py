#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 08:18:07 2020

"""

import requests
from bs4 import BeautifulSoup
import time
import traceback


def fetchHotel(url):
    # 发起网络请求，获取数据
    headers = {
        'accept': '*/*',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'referer': 'https://travel.qunar.com/travelbook/list/22-shanghai-299878/hot_heat/2.htm',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': 'QN1=00002a80306c231a2c58be6d; QN300=auto_4e0d874a; QN99=6292; QunarGlobal=10.86.213.148_-2b1256aa_171d2b1b886_115e|1588379532107; QN601=bbc4e7c69b141149cb4024bf2efc46b0; _i=DFiEuZrHUEwwKkX6-MrCA3RIAPtw; QN48=tc_51f987b8a4f1c238_171d2cc4730_5aee; fid=5cb36630-c30c-4ef5-8bca-190f35759e48; QN57=15884300517000.36608813248313266; QN58=1588430051698%7C1588430234381%7C6; QN205=partner; QN277=partner; QN269=78ED86708C0C11EA916CFA163E1A7091; QN25=e64f0ce8-7036-475b-b946-89bac32f073c-9f992f90; QN43=2; QN42=paug9124; _q=U.vcqusvq7037; _t=26785461; csrfToken=dRkcJPzQvafplyVabnxpfS1wy9EzCvnz; _s=s_ZIEW45QUGTERF2EU26C7ALGRXE; _v=HpRLcSY-xUFM5w1bZfZW1_Ry0u7zOytHn1g7oOxVyGBSSUcmZedYeZe3LHj90RRMWp6lTP3_Fx5e3-T1NVYqAdlbNvOjj-jltF7EDeXg0prU7UQiOr4g-IEL_HvpoXQsehnohmkwro25C0RpnropwuCwQ5x2GuGiN0rUiR7Ix_Nh; _vi=v4sTzPGRV6eBIIatgjFDUVd3_szD58JwGHeSl13go4eM23xj58IVpclMzIbPwIkuBdK6rw_oDVUpjFUURe37nsRBLqGDqmDZdtGNXsCmkMB214NI2B4PSSNvBvN1lIbfu7FVhGK6kIKkIkEQTgjUBaLjp1Hpx-MjoQhEppC5qY4m; QN44=vcqusvq7037; QN163=0; Hm_lvt_c56a2b5278263aa647778d304009eafc=1592611618,1592611938,1592612533; QN271=eb9b3688-2a94-4159-b1ad-def815a78b10; Hm_lpvt_c56a2b5278263aa647778d304009eafc=1592612621; QN267=0337375417ba3e9b2c',
    }
    r = requests.get(url, headers=headers)
    r.encoding = "utf-8"
    return r.text


def getPageNum(html):
    # 获取总页数
    pageNum = 1
    bsObj = BeautifulSoup(html, "html.parser")
    pageList = bsObj.find("div", attrs={"class": "b_paging"}).find_all("a")
    if (pageList):
        pageNum = pageList[-2].text
    return int(pageNum)


def parseHtml(html):
    # 解析html网页，提取数据
    bsObj = BeautifulSoup(html, "html.parser")
    global bookList
    bookList = bsObj.find("ul", attrs={"class": "b_strategy_list"})
    books = []

    for book in bookList:
        # 链接
        link = "https://travel.qunar.com" + book.h2.a["href"]
        # 标题
        title = book.h2.a.text
        places = book.findAll("p", attrs={"class": "places"})
        # 行程
        if len(places) > 1:
            trip_places = places[1].text
        else:
            trip_places = places[0].text

        user_info = book.find("p", attrs={"class": "user_info"})
        intro = user_info.find("span", attrs={"class": "intro"})
        # 作者
        user_name = intro.find("span", attrs={"class": "user_name"}).text
        # print("user_name:",user_name)
        date = intro.find("span", attrs={"class": "date"}).text
        # 天数
        days = intro.find("span", attrs={"class": "days"}).text
        # 照片数
        photoTmp = intro.find("span", attrs={"class": "photo_nums"})
        if (photoTmp):
            photo_nums = photoTmp.text
        else:
            photo_nums = "没有照片"
        # 人数
        peopleTmp = intro.find("span", attrs={"class": "people"})
        if (peopleTmp):
            people = peopleTmp.text
        else:
            people = ""
        # print("people:",people)
        # 玩法
        tripTmp = intro.find("span", attrs={"class": "trip"})
        if (tripTmp):
            trip = tripTmp.text
        else:
            trip = ""
        # 费用
        feeTmp = intro.find("span", attrs={"class": "fee"})
        if (feeTmp):
            fee = feeTmp.text
        else:
            fee = ""
        # print("fee:",fee)

        nums = user_info.find("span", attrs={"class": "nums"})
        # 阅读数
        icon_view = nums.find("span", attrs={"class": "icon_view"}).span.text
        # 点赞数
        icon_love = nums.find("span", attrs={"class": "icon_love"}).span.text
        # 评论数
        icon_comment = nums.find("span", attrs={"class": "icon_comment"}).span.text
        books = [[title, link, user_name, date, days, photo_nums, people, trip, fee, icon_view, icon_love, icon_comment,
                  trip_places]]
        yield books


def saveCsvFile(filename, content):
    import pandas as pd
    # 保存文件
    dataframe = pd.DataFrame(content)
    dataframe.to_csv(filename, encoding='utf_8_sig', mode='a', index=False, sep=',', header=False)


def downloadBookInfo(url, fileName, city_code):
    head = [["标题", "链接", "作者", "出发日期", "天数", "照片数", "人数", "玩法", "费用", "阅读数", "点赞数", "评论数", "行程"]]
    saveCsvFile(fileName, head)
    html = fetchHotel(url)
    pageNum = getPageNum(html)
    print(pageNum)
    for page in range(1, pageNum + 1):
        time.sleep(2)
        try:
            print("正在爬取", str(page), "页 .......")
            url = "https://travel.qunar.com/travelbook/list/" + str(city_code) + "/hot_heat/" + str(page) + ".htm"
            html = fetchHotel(url)
            for book in parseHtml(html):
                saveCsvFile(fileName, book)
        except Exception:
            print(traceback.format_exc())
            print("第%d页发生错误" % (page))


data_dict = {
    '三亚': '22-sanya-300188'
}

for i in data_dict.keys():
    fileName = "%s_data.csv" % (i)
    url = "https://travel.qunar.com/travelbook/list/%s/hot_heat/1.htm" % (i)
    downloadBookInfo(url, fileName, data_dict[i])
    print("%s全部完成" % (i))