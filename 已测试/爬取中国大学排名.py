import requests
from bs4 import BeautifulSoup
import csv
allUniv = []
def getHTMLText(url):
    try:
        r =requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding="utf-8"
        return r.content.decode('utf-8')
    except:
        return ""

def fillUnivList(soup):#这个网站又改了，我靠
    data =soup.find_all("tr")
    for tr in data:
        ltd = tr.find_all("td")
        # print(ltd)
        if len(ltd)==0:
            continue
        singleuniv =[]
        # sing = []
        for td in ltd:
            #print(td.text)
            singleuniv.append(td.text.strip().replace('\n',''))
        print(singleuniv)
        allUniv.append(singleuniv)#这里有自己写的代码哦，这个我必须学会！
def printUnivList(num):
    print("{}\t{}\t{}\t{}\t{}\t{}\t\n".format("排名","学校名称","省市","类型","总分","生源质量"))
    for i in range(num):
        u = allUniv[i]
        print("{}\t{}\t{}\t{}\t{}\t{}\t\n".format(u[0],u[1],u[2],u[3],u[4],u[5]))
def main(num):
    url ="https://www.shanghairanking.cn/rankings/bcur/201911"
    html = getHTMLText(url)
    soup = BeautifulSoup(html,"html.parser")
    fillUnivList(soup)
    printUnivList(num)

main(5)
print(len(allUniv))
with open("大学排名.csv", "w",newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["排名", "学校名称", "省市", "总分", "指标得分"])
    for row in allUniv[:100]:
        writer.writerow(row)

#这便是一个简单的爬虫了，加油！