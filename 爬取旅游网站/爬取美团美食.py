# import requests
# import re
#
# def start():
#     for w in range(0, 1600, 32):
#         try:
#             # 注意uuid后面参数空余将uuid后xxx替换为自己的uuid参数
#             url = 'https://apimobile.meituan.com/group/v4/poi/pcsearch/1?uuid=xxx&userid=-1&limit=32&offset='+str(w)+'&cateId=-1&q=%E7%81%AB%E9%94%85'
#             #headers的数据可以在F12开发者工具下面的requests_headers中查看，需要实现选择如下headers信息
#             #必要情况  请求频繁 建议增加cookie参数在headers内
#             headers =  {
#                 'Accept': '*/*',
#                 'Accept-Encoding': 'gzip, deflate, br',
#                 'Accept-Language': 'zh-CN,zh;q=0.9',
#                 'Connection': 'keep-alive',
#                 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400',
#                 'Host': 'apimobile.meituan.com',
#                 'Origin': 'https://bj.meituan.com',
#                 'Referer': 'https://bj.meituan.com/s/%E7%81%AB%E9%94%85/'
#             }
#             response = requests.get(url, headers=headers)
#             #正则获取当前响应内容中的数据，因json方法无法针对店铺特有的title键值进行获取没所以采用正则
#             titles = re.findall('","title":"(.*?)","address":"', response.text)
#             addresses = re.findall(',"address":"(.*?)",', response.text)
#             avgprices = re.findall(',"avgprice":(.*?),', response.text)
#             avgscores = re.findall(',"avgscore":(.*?),',response.text)
#             comments = re.findall(',"comments":(.*?),',response.text)
#             #输出当前返回数据的长度  是否为32
#             print(len(titles), len(addresses), len(avgprices), len(avgscores), len(comments))
#             for o in range(len(titles)):
#             #循环遍历每一个值  写入文件中
#                 title = titles[o]
#                 address = addresses[o]
#                 avgprice = avgprices[o]
#                 avgscore = avgscores[o]
#                 comment  = comments[o]
#             file_data(title, address, avgprice, avgscore, comment)
#
# #文件写入方法
# def file_data(title, address, avgprice, avgscore, comment):
#     data = {
#         '店铺名称': title,
#         '店铺地址': address,
#         '平均消费价格': avgprice,
#         '店铺评分': avgscore,
#         '评价人数': comment
#     }
#     with open('美团美食.txt', 'a', encoding='utf-8') as fb:
#         fb.write(data)
#         #ensure_ascii=False必须加因为json.dumps方法不关闭转码会导致出现乱码情况
# if __name__ == '__main__':
#     start()