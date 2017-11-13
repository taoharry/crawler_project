#!usr/bin/env python
# coding:utf-8

import urllib,urllib2
import re
import sys
from sqlalchemy.orm import sessionmaker


from BaseObj import BaseObj
from BaseDate import BaseData
from utills.crawlerUtiles import formatUrl
from utills.sqlutils import basicInfo
reload(sys)
sys.setdefaultencoding('utf-8')

HostList = '<ul id="houseList">[\s\S]*?</ul>'
LI = '<li class="clearfix">[\s\S]*?</li>'

class Ziru(BaseObj):

    def __init__(self):
        #暂且保留留作任务模块
        #pass
        self.dt = {}

    def getPage(self,url):
        '''
        每一页内容
        http://www.ziroom.com/z/nl/z3.html?qwd=%E5%8C%97%E4%BA%AC&p=2
        :return: none
        '''
        html = self.getPageContent(url)
        ul = self.reSearch(HostList,html,0)
        lis = re.findall(LI,ul)
        #print "name,location,area,tier,usearea,traffic_distance,icons,subway,balcony,publish,price,price_way"
        for li in lis:
            imageUrl = self.reSearch('<img src="([\s\S]*?)"',li,1)
            name = self.reSearch('<a.*?class="t1".*?>(.*?)</a>',li,1)
            location = self.reSearch('<h4[\s\S]*?target.*?>(.*?)</a>',li,1)
            innerUrl = self.reSearch('<a target.*?href="(.*?)"',li,1)
            span = re.findall('<span>(.*?)</span>',li)
            if len(span) ==4:
                area,tier,usearea,traffic_distance = span[0],span[1],span[2],span[3]
            icons = self.reSearch('<span class="icons">(.*?)</span>',li,1)
            subway = re.findall('<span class="subway">(.*?)</span>',li)
            balcony = self.reSearch('<span class="balcony">(.*?)</span>',li,1)
            publish = self.reSearch('<span class="style">(.*?)</span>',li,1)
            price = self.reSearch('<p class="price">([\s\S]*?)<span',li,1)
            price_way = self.reSearch('<span class="gray-6">\((.*?)\)</span>',li,1)
            data = BaseData()
            data.image = formatUrl(imageUrl)
            data.innerUrl = formatUrl(innerUrl)
            data.name = name
            data.location = location
            data.area = area
            data.tier = tier
            data.usearea = usearea
            data.traffic_distance = traffic_distance
            data.icons = icons
            data.subway = subway
            data.balcony = balcony
            data.publish = publish
            data.price = price.split()
            data.price_way = price_way
            import pprint,json
            #print json.dumps(data.__dict__, ensure_ascii=False)

            t = (name,location,area,tier,usearea,traffic_distance,icons,','.join(subway),balcony,publish,''.join(price.split()),price_way)
            self.dt[t] = None


    #这里准备做第二张表格，里面是详细信息，声明其他类，有需求了在做。
    def getHomepage(self,url):
        html = self.getPageContent(self.url)
        pass



    def main(self,url,keyword,num=99):
        if not isinstance(num,int):
            num = 20
        if url == '':
            for i in range(num):
                url = 'http://www.ziroom.com/z/nl/z3.html?qwd={keyword}&p={page}'.format(keyword=keyword,page=i)
                self.getPage(url)
        else:
            self.getPage(url)
        from  utills.exalutils import writeXl
        writeXl('ziru.xls',self.dt )
if __name__ == "__main__":
    url = 'http://www.ziroom.com/z/nl/z3.html?qwd=%E5%8C%97%E4%BA%AC&p=2'
    Ziru().main(url='',keyword='北京')

