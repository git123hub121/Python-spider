import requests
from lxml import etree

#爬取lol壁纸，其他游戏壁纸也可以哦
class ImageSpider(object):
    def __init__(self):
        #http://www.netbian.com/s/wangzherongyao/
        self.firsr_url = "http://www.netbian.com/s/lol/index.htm"
        self.url = "http://www.netbian.com/s/lol/index_{}.htm"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
        }

    '''发送请求  获取响应'''

    def get_page(self, url):
        res = requests.get(url=url, headers=self.headers)
        html = res.content.decode("gbk")
        return html

    '''解析数据'''

    def parse_page(self, html):
        parse_html = etree.HTML(html)
        image_src_list = parse_html.xpath('//div[@class="list"]/ul/li/a//@href')

        for image_src in image_src_list:
            fa = "http://www.netbian.com" + image_src
            # print(fa)
            html1 = self.get_page(fa)  # 第二个发生请求
            parse_html1 = etree.HTML(html1)
            # print(parse_html1)

            bimg_url = parse_html1.xpath('//div[@class="pic-down"]/a/@href')
            for i in bimg_url:
                diet = "http://www.netbian.com" + i
                # print(diet)
                html2 = self.get_page(diet)
                parse_html2 = etree.HTML(html2)
                # print(parse_html2)
                url2 = parse_html2.xpath('//table[@id="endimg"]//tr//td//a/img/@src')
                for r in url2:
                    pass
                    # print(r)
                filename = parse_html2.xpath('//table[@id="endimg"]//tr//td//a/@title')
                # print(url2)
                for e in filename:
                    # print(e)
                    dirname = "./lol/" + e + '.jpg'
                    html2 = requests.get(url=r, headers=self.headers).content
                    # print(html2)
                    print(dirname)
                    with open(dirname, 'wb') as f:
                        f.write(html2)
                        print("%s下载成功" % filename)

    def main(self):
        startPage = int(input("起始页:"))
        endPage = int(input("终止页:"))
        for page in range(startPage, endPage + 1):
            if page == 1:
                url = self.firsr_url

            else:
                url = self.url.format(page)
            # print(url)
            html = self.get_page(url)
            print("第%s页爬取成功！！！！" % page)
            # print(html)
            self.parse_page(html)


if __name__ == '__main__':
    imageSpider = ImageSpider()
    imageSpider.main()

#一系列游戏壁纸皆可  彼岸图网    彼岸桌面

#下面是我写的，又浪费时间了
# import requests
# from lxml import etree
# start_page = int(input("起始页：\n"))
# end = int(input("终止页：\n"))
# for i in range(start_page,end+1):
#     if i == 1:
#         new_url = "http://www.netbian.com/s/lol/index.htm"
#     else:
#         new_url = f'http://www.netbian.com/s/lol/index_{i}.htm'
#     headers = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
# }
#     req = requests.get(url=new_url,headers=headers).content.decode('gbk')#这里不能 utf-8
#     html = etree.HTML(req)
#     imgStr = html.xpath('//div[@class="list"]/ul/li/a//@href')#得到的是一个列表
#     # print(imgStr)
#     count = 0
#     for imgstr in imgStr:
#         new_str = "http://www.netbian.com"+imgstr
#         #print(new_str)
#         #仔细观察，如果想要获取到原图，需要找到其完整的图片链接，通过F12工具可以得知，此图片最终链接由第三部分构成
#         html_1 = requests.get(url=new_str,headers=headers).content
#         imghtml = etree.HTML(html_1).xpath('//div[@class="pic"]/p/a//@href')
#         for bigimg in imghtml:
#             #最终图片链接
#             big_img = "http://www.netbian.com"+bigimg
#             # print(big_img)
#             html_2 = requests.get(url=big_img,headers=headers).content
#             # print(html_2)
#             img = etree.HTML(html_2).xpath('//td/a/img//@src')
#             for i in img:#每个img里面只有一张图片
#                 count += 1
#                 #print(type(i))#<class 'lxml.etree._ElementUnicodeResult'>
#                 i = requests.get(url=i,headers=headers).content
#                 #print(type(i))#<class 'bytes'>
#                 imgname = etree.HTML(html_2).xpath('//td/a/img//@title')[0]
#                 savepath = "壁纸/"+ imgname + '.jpg'#图片重命名，需要自己新建一个‘壁纸’文件夹
#                 print(count,"---",savepath)
#                 with open(savepath,'wb') as f:
#                     f.write(i)
#     print('==========')