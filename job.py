import requests
import pandas as pd
from lxml import etree
from urllib.error import HTTPError,URLError



def getHtml(url):
    #携带请求头信息，否则无法获取数据
    headers={"User-Agent":"Mozilla/5.0"}
    try:
        response=requests.get(url,headers=headers)
    except(HTTPError, URLError) as e:
        return None
    return response.text
def parseHtml(html):
    tree=etree.HTML(html)
    positions=tree.xpath('//div[@class="job-title"]/text()')
    companies=tree.xpath('//div[@class="company-text"]/h3[@class="name"]/a/text()')
    salarys=tree.xpath('//div[@class="info-primary"]/h3/a/span/text()')
    years =tree.xpath('//div[@class="info-primary"]/p/text()[2]')
    didian =tree.xpath('//div[@class="info-primary"]/p/text()[1]')
    releasetime=tree.xpath('//div[@class="info-publis"]/p/text()')
    return positions,companies,salarys,releasetime,years, didian
def go():
    position=[]
    companies=[]
    releasetime=[]
    salarys=[]
    years = []
    didian = []
    postion = '机器学习'
    for i in range(10):
        url = "https://www.zhipin.com/c101020100/h_101020100/?query=" + postion + "&page="+str(1+i)+"&ka=page-"+str(i+1)
        print(url)
        html = getHtml(url)
        if html !=None:
            p, c, s, r, y,d = parseHtml(html)
            position += p
            companies += c
            salarys += s
            releasetime += r
            years += y
            didian += d
    dic = {"职位": position, "公司": companies,"地点":didian,"工作年限":years, "薪水":salarys, "发表时间": releasetime}
    df = pd.DataFrame(dic)
    df.to_excel(postion + '.xlsx', index=False)

if __name__ == '__main__':
     go()
     print("数据写入完毕!")
