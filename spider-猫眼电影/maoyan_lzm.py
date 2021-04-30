#任务：爬取猫眼top100
#1.导入包   2.设置headers   3.利用requests导入html  4.进行正则表达式匹配    5.先以列表、元祖形式输出
#6.发现链接规律，设置链接循环   7.将其转化为字典输出 json对象转化为json字符串   8.以追加的方式存入文本  9.设置时间缓冲
import re
import requests
import time
import json

for i in range(10):
    index = i*10
    url = "https://maoyan.com/board/4?offset={}".format(index)
    print("请求url：" + url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    html = requests.get(url=url,headers=headers).text
    pattern = re.compile(r'<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern,html)
    # print(items)
    # for i in a:
    # i1 = i[3]+i[4]
    # print(i1)
    # b = i[:3]
    # b.append(i1)
    # print(b)
    item_ = []
    for item in items:
        item =list(item)
        item_s = item[5]+item[6]
        item_ = item[:5]
        item_.append(item_s)
        print(item_)
        with open('D:\Python\Mypython\Python爬虫\spider-猫眼电影\maoyan1.txt','a',encoding='utf-8') as f:
            f.write(",".join(item_).strip()+"\n")
  
if __name__ == '__main__':
    time.sleep(1)
    
    

#yield  是函数内部构造，不能放在外面 因此我们简写失败
#原理也可以实现，代码也很简写，但是可读性不高，并且也存在数据读取不全的问题，但是代码比较OK了，先理解，以后慢慢发现完善
