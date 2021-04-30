# 网络爬虫之爬取糗事百科段子实战
import urllib.request
# import urllib.error
import re
# 糗事百科官网网址
# url="https://www.qiushibaike.com/text/"
# 采用浏览器伪装技术，先设置报头
# 爬取前20网页信息
for i in range(0, 20):
    # 异常处理
    # try:
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69'}
        # 构造每一页的网址
    this_url="https://www.qiushibaike.com/text/page/"+str(i+1)+"/"
    req = urllib.request.Request(this_url,headers=headers)
        # 读取每一页的数据
    data=urllib.request.urlopen(req).read().decode('utf-8')
        # 设置正则表达式
    pat='<div class="content">.*?<span>(.*?)</span>'
        # 进行信息提取，因为有换行符，所有要用re.S按.能匹配换行符
    this_data=re.compile(pat, re.S).findall(data)
    for d in this_data:
        print(d.strip())  # 字符串的前面和后面有的有换行符，可以用strip()方法去掉字符串首位处的换行符和空格
        print('--------------------------------------')    
    # except urllib.error.HTTPError as e:
    #     if hasattr(e, 'code'):
    #         print(e.code)
    #     if hasattr(e, 'reason'):
    #         print(e.reason)
    #先放这里
    


