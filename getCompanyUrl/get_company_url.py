# -*- coding: utf-8 -*-
import MySQLdb
'''
fetch url and return lists

'''
class get_company_url():
    def get_company_url(self, index_time):
        db=MySQLdb.connect("localhost","root","wwd","spider",charset='utf8')
        cursor=db.cursor()
        a=0
        b=20
        lists=[]
        for x in range (1,index_time):
            sql='select url from company limit %s,%s'%(a,b)
            cursor.execute(sql)
            data=cursor.fetchall()
            for y in range(0,20):
                href=str(data[y]).replace("(u'","").replace("',)","")
                lists.append(href)
            a+=20
        db.close()
        return lists
