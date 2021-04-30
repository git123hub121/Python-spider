import re
import json
import time
import urllib.request

# 创建发起请求
# 返回网页文本


def get_page(url):
    try:
        # 请求头
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
        }

        # 创建请求
        req = urllib.request.Request(url=url, headers=headers)

        # 发起请求，得到相应
        res = urllib.request.urlopen(req)

        if res.getcode() == 200:
            # 返回页面文本
            return res.read().decode("utf-8")
        return None
    except BaseException as e:
        return None


# 解析页面 正则
def parge_page(html_text):
    # pattern = re.compile(r'<dd>.*?board-index.*?(\d+)</li>.*?<img data_src="(.*?)".*?="name"><a.*?>(.*?)</a>.*?"star">(.*?)</p>.*?"releasetime">(.*?)</p>*?"interger">(.*?)</i>.*?"faraction">(.*?)</i>', re.S)
    pattern = re.compile(
        r'<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)

    # 匹配
    items = re.findall(pattern, html_text)
    print(items)
    # print()

    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5] + item[6]
        }


# 写入文件
def write_to_file(item):
    with open('./猫眼电影Top100.txt', 'a',encoding='utf-8') as fp:
        fp.write(json.dumps(item, ensure_ascii=False) + '\n')


# 主函数
def main(offset):
    # 请求url
    url = "https://maoyan.com/board/4?offset={}".format(offset)
    print("请求url：" + url)

    # 创建发起请求
    html_text = get_page(url)
    # print(html_text)

    # 解析文本
    # 得到的items是一个列表
    # 列表里面有十条数据
    # 每一页就是items
    # 然后将每一页的10条数据存入生成器
    # 然后这个生成器作为返回值传给外面的变量

    items = parge_page(html_text)
    # print(type(items))

    # 写入文件
    for item in items:
        # print("item: " + item)
        write_to_file(item)


if __name__ == '__main__':
    for i in range(10):
        main(i*10)
        time.sleep(1)

#以字典形式保存数据