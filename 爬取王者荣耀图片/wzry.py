import requests
import os

url = 'https://pvp.qq.com/web201605/js/herolist.json'
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'
}
reponse =requests.get(url=url,headers=header)
hero_list = reponse.json()#这个方法要查一下 见txt 用来对json格式的响应体进行反序列化 转为字典,看着没啥变化，但是就是将格式转变了
#print(hero_list)
#如果不用map函数来写，就这样写，对比一下，还是多学点语法有好处
# name = []
# for i in range(len(hero_list)):
#     hero_name = hero_list[i]['cname']#cname英雄名字      **map()** 会根据提供的函数对指定序列做映射。
#     #print(hero_name)
#     name.append(hero_name)
# print(name)
her0_name = list(map(lambda x: x['cname'],hero_list))
hero_number = list(map(lambda x:x['ename'],hero_list))#ename对应编号
hero_title = list(map(lambda x:x['title'],hero_list))
# skin_name = list(map(lambda x:x['skin_name'].split('|'),hero_list))
def save_IMG():
    num = 0
    count = 0
    h_l = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/'
    for i in hero_number:#列表是可遍历对象
        print('='*10)
        num = num+1
        print(num,hero_name[num-1],hero_title[num-1])
        # print(num,name[num-1],hero_title[num-1])
        for sk_num in range(15):
            hsl = h_l+str(i)+'/'+str(i)+'-bigskin-'+str(sk_num)+'.jpg'
            hl = requests.get(hsl) #这一步只是得到了响应，所以才有下面的if判断 可以尝试输出hl查看
            if hl.status_code == 200:
                count =count+1
                print(count,hsl)
                # print(skin_name[count-1])
            # 
                # 将图片保存下来，并以"英雄名称_皮肤序号"方式命名
                
                # with open('image/'+hero_name[num]+str(sk_num)+'.jpg','wb') as f:
                    # f.write(hl.content)   
    print("总共下载"+count+"张皮肤图片！！！")    
save_IMG()


#由于马超没有skin_name参数，所以会出现KeyError: 'skin_name'报错，故暂时不统计皮肤名字！
#大佬爬取链接，可参考：https://blog.csdn.net/u014361280/article/details/104236704
