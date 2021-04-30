import requests
import json
import re
import pandas as pd
url='https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=fsnd&rowcode=reg&colcode=sj&wds=%5B%7B%22wdcode%22%3A%22zb%22%2C%22valuecode%22%3A%22A080101%22%7D%5D&dfwds=%5B%7B%22wdcode%22%3A%22sj%22%2C%22valuecode%22%3A%22LAST20%22%7D%5D&k1=1601122489572'
headers={'User-Agent':'User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'}
response=requests.get(url, headers=headers, verify=False)
results=json.loads(response.text)
cityTocodes={}
for i in results['returndata']['wdnodes'][1]['nodes']:
    cityTocodes[i['code']]=i['cname']
print(cityTocodes)
codes=[]
data = []
datas = []
for i in results['returndata']['datanodes']:
    pattern=re.compile(r'zb\.A080101_reg\.(\d+)_sj\.(\d+)')
    code=re.findall(pattern, i['code'])[0][0]
    if code not in codes:
        codes.append(code)
        datas.append(data)
        data=[]
    data.append(i['data']['data'])
print(datas)
years=list(range(2000,2020))[::-1]
datas.append(data)
citys=[cityTocodes[i] for i in codes]
city_datas=pd.DataFrame(datas[1:], columns=years, index=citys)
city_datas.to_excel('全国各省财政收入.xlsx')