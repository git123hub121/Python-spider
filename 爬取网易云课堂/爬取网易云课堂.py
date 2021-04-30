import requests
import pandas as pd
(productId,productName,provider,imgUrl,info,learnerCount,lessonCount,originalPrice,machineGrade) = ([],[],[],[],[],[],[],[],[])
for index in range(8):
    url = 'https://study.163.com/p/search/studycourse.json'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.52'
    }
    payload = {
        'activityId': 0,
        'keyword': "python",
        'orderType': 50,
        'pageIndex': 1+index,
        'pageSize': 50,
        'priceType': -1,
        'qualityType': 0,
        'relativeOffset': 0,
        'searchTimeType': -1
    }
    # req = requests.get(url=url,headers=headers)#get不行
    req = requests.post(url=url,json=payload,headers=headers)
    content_json = req.json()
    #输出发现，数据并不完全
    content_json['code']#json上对应的key是可以调用的
    # len(content_json)
    #content_json
    # len(content_json['result']['list'])
    #totalpage = content_json['result']['query']['totlePageCount'] 为方便，我就不写成函数了，偷一下懒，直接写8了
    # info_list = []
    for i in range(len(content_json['result']['list'])):
        # getinfo = []
        pId = content_json['result']['list'][i]['productId']
        pName = content_json['result']['list'][i]['productName']
        pder = content_json['result']['list'][i]['provider']
        img = content_json['result']['list'][i]['imgUrl']
        inf = content_json['result']['list'][i]['description']
        lCount = content_json['result']['list'][i]['learnerCount']
        lesCount = content_json['result']['list'][i]['lessonCount']
        Price = content_json['result']['list'][i]['originalPrice']
        mGrade = content_json['result']['list'][i]['machineGrade']
        if inf != None:
            inf = inf.replace('\n','').replace('*','').replace('【','').replace('】','').replace(' ','').replace('=','')
        # #1
        # getinfo.append(pId)
        # getinfo.append(pName)
        # getinfo.append(pder)
        # getinfo.append(img)
        # getinfo.append(inf)
        # getinfo.append(lCount)
        # getinfo.append(lesCount)
        # getinfo.append(Price)
        # getinfo.append(mGrade)

        # info_list.append(getinfo)
        #2
        productId.append(pId)
        productName.append(pName)
        provider.append(pder)
        imgUrl.append(img)
        info.append(inf)
        learnerCount.append(lCount)
        lessonCount.append(lesCount)
        originalPrice.append(Price)
        machineGrade.append(mGrade)
    # info_list[:3]
# print(productId)
data_list = {
    'cid' : productId,
    'cname' : productName,
    'cp' : provider,
    'img' : imgUrl,
    'info' : info,
    'study_c' : learnerCount,
    'les_c' : lessonCount,
    'price' : originalPrice,
    'mg' : machineGrade
}
    #1.保存数据---join
    # import csv
    # name = ['cid','cname','cp','img','info','study_c','les_c','price','mg']
    # with open('网易云.csv','w',encoding='utf-8',newline='') as f:
    #     savedata = csv.writer(f, delimiter=',')#分隔符设置
    #     savedata.writerow(name)#添加表头
    #     for data in info_list:
    #         savedata.writerow(data)
            # print(data)
    #2.pd
pd.DataFrame(data = data_list).to_excel('网易云课堂-python.xlsx',index = None)

#还是有空值，因为有些数据为空
'''对于json数据，由于都是同一个url，所以分页的规律不是url，而是在payload里面，
通过观察，可以发现变动的规律是pageIndex，并且在总页数参数在json中，是totlePageCount: 8，
测试发现第8页只有11个数据，50x7+11+1=362，没有数据遗漏，nice！
'''