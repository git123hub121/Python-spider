import re
import requests
import urllib.request
import os
import time

#目前只能爬取一页，而且现在找不到传统翻页了！-> 已完成搜索与页数爬取，需要去观察气ajax的参数值变化！
start = time.time()
#long running
#do something other
path = 'C:/Users/Administrator/Pictures/Python图片/百度图片/'
word = input("请输入你要搜索的关键词：  ")

def imgURL(word):
    count = 0
    if not os.path.exists(path+word):
        os.mkdir(path+word)
    #pages = input("请输入你要爬取的页数：（温馨提示：每页有30张图片！）")
    page_start = int(input("请输入起始页---[默认从1开始]：   "))
    page_end = int(input("请输入终止页---[温馨提示：终止页将不会爬取]：  "))
    page = page_end-page_start
    print(f"你将爬取{page}页")
    if page_end > 50:
        print("超出最大限制,请重新输入：    ")
        page_end = int(input("请输入终止页： ---为避免服务器负载，请将max控制在50以内---    "))
    print("已为你找到关键词---"+word+"---的图片,即将开始下载......")
    print("-"*20)
    for page in range(page_start-1,page_end-1): #int(pages)
        # pn代表翻页，每30张图片为1页  0   30   60   90 ....
        url = f'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&word={word}&pn={str(page*30)}'
        headers = {
            "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 Edg/86.0.622.63"
        }
        res = requests.get(url,headers=headers).text
        for img in re.findall('"objURL":"(.*?)",',res):
            try:
                count += 1
                print(f'图片正在下载---第{count}张：图片地址：{img}',"\t")  #print(img[7:-5])
                urllib.request.urlretrieve(img,path+word+'/'+str(count)+'.jpg')   #   '.jpg'  +str(img[7:-5])+
                #这个是不能自己创建文件夹的，我靠了！
            except:
                continue
    return count
total_count = imgURL(word)
print("-"*20)
print(f"图片爬取/保存成功！图片保存路径：{path+word}  共计下载了{total_count}张")
print("-"*20)
go = input("是否继续爬取！")
if go == 'yes':
    imgURL(word)
elif go == 'no':
    print("真的要离开吗？人家舍不得吗？")
    time.sleep(5)
    print('好啦！逗你玩的哦\n')
else:
    print('好啦！逗你玩的哦\n当前搜索结束，感谢使用')
print("-"*20)
end = time.time()
print(f"程序用时{end - start}秒，棒棒哒")
#改进这个，实现搜索爬取！需要将word以及pn进行操作