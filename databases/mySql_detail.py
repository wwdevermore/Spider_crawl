# -*- coding: utf-8 -*-
import urllib2
import MySQLdb
from scrapy.selector import Selector
from getProxyAddress import get_proxy_address
from getUserAgent import get_user_agent
from getCompanyUrl.get_company_url import get_company_url

'''
fetch company url
And crawl details

'''

getUrl=get_company_url()
lists=getUrl.get_company_url(4)

db=MySQLdb.connect("localhost","root","wwd","spider",charset='utf8')
cursor=db.cursor()

address = get_proxy_address.get_proxy_address()
agents = get_user_agent.get_user_agent()
proxy = address.get()
agent = agents.get()
proxy_handler = urllib2.ProxyHandler(proxy)
opener = urllib2.build_opener(proxy_handler)

for href in lists:
    url = "https://"+href
    req = urllib2.Request(url)
    req.add_header('User-Agent', agent)
    urllib2.install_opener(opener)
    html = urllib2.urlopen(req)
    page = html.read()

    company_type=Selector(text=page).xpath('//*[@id="basic_container"]/div[2]/ul/li[1]/span/text()').extract()
    company_finacing=Selector(text=page).xpath('//*[@id="basic_container"]/div[2]/ul/li[2]/span/text()').extract()
    company_area=Selector(text=page).xpath('//*[@id="basic_container"]/div[2]/ul/li[4]/span/text()').extract()
    company_people=Selector(text=page).xpath('//*[@id="basic_container"]/div[2]/ul/li[3]/span/text()').extract()
    company_rate=Selector(text=page).xpath('/html/body/div[3]/div/div/div[2]/ul/li[2]/strong/text()').extract()
    company_days=Selector(text=page).xpath('/html/body/div[3]/div/div/div[2]/ul/li[3]/strong/text()').extract()
    company_name=Selector(text=page).xpath('/html/body/div[3]/div/div/div[1]/h1/a/text()').extract()

    detail=[]
    detail.append(company_name[0].strip())
    detail.append(company_area[0].strip())
    detail.append(company_people[0])
    detail.append(company_finacing[0])
    detail.append(company_days[0].strip())
    detail.append(company_rate[0].strip())
    detail.append(company_type[0].strip())

    sql='''insert into com_detail
    (company_name,company_area,company_people,company_finacing,company_days,company_rate,company_type)
    values
    ("%s","%s","%s","%s","%s","%s","%s")''' %(detail[0],detail[1],detail[2],detail[3],detail[4],detail[5],detail[6])
    cursor.execute(sql)
    db.commit()
db.close()