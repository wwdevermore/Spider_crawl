# -*- coding: utf-8 -*-
import MySQLdb
import urllib2

from getProxyAddress import get_proxy_address
from getUserAgent import get_user_agent
from lxml import etree



def save_companies():
    db = MySQLdb.connect("localhost", "root", "wwd", "spider", charset="utf8")
    cursor = db.cursor()
    address = get_proxy_address.get_proxy_address()
    agents = get_user_agent.get_user_agent()
    proxy = address.get()
    agent = agents.get()
    proxy_handler = urllib2.ProxyHandler(proxy)
    opener = urllib2.build_opener(proxy_handler)

    for number in range (1,21):
        print "page No. %s  starting" % number
        url = 'https://www.lagou.com/gongsi/0-0-0?first=false&pn=%s&sortField=0&havemark=0' % number
        req = urllib2.Request(url)
        req.add_header('User-Agent', agent)
        urllib2.install_opener(opener)
        html = urllib2.urlopen(req)
        page=html.read().decode('utf-8')
        selecter=etree.HTML(page)

        Company_name_xpath ='//*[@id="company_list"]/ul/li[position()<17]/dl/dd/h3/a/text()'
        Company_link_xpath ='//*[@id="company_list"]/ul/li[position()<17]/dl/dd/h3/a/@href'
        Company_name = selecter.xpath(Company_name_xpath)
        Company_link = selecter.xpath(Company_link_xpath)

        for x in range(0,16):
            try:
                Company_links =str(Company_link[x]).replace("//", "")
                sql = "insert into company (companyname,url) values('%s','" % Company_name[x] + "%s')" % Company_links
                cursor.execute(sql)
                db.commit()
                print "saving company %s" % Company_name[x]
            except Exception,e:
                print "Done:",e
                return "SUCCESS"



    db.close()

save_companies()