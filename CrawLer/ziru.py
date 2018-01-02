#!usr/bin/env python
# coding:utf-8

import urllib,urllib2
import re,os
import sys,time,random
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append("/home/harry/ENV")
execPath = os.path.dirname(os.path.abspath("__file__"))
appPath = os.path.dirname(execPath)
sys.path.append(appPath)


from CrawLer.BaseObj import BaseObj
from CrawLer.BaseDate import BaseData
from utills.crawlerUtiles import formatUrl
from utills.logUtiles import logUtils
#from utills.timeUtils import Sleep


HostList = '<ul id="houseList">[\s\S]*?</ul>'
LI = '<li class="clearfix">[\s\S]*?</li>'
log = logUtils()

class Ziru(BaseObj):

    def __init__(self):
        #暂且保留留作任务模块
        #pass
        self.channel = 'ziru'
        self.dt = {}

    def getPage(self,url,keyword):
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
            data.keyword = keyword
            data.channel = self.channel
            data.image = formatUrl(imageUrl)
            data.innerUrl = formatUrl(innerUrl)
            data.name = name
            data.location = location
            data.area = filter(str.isdigit,area).strip()
            data.tier = tier
            data.usearea = usearea
            data.traffic = traffic_distance
            data.icons = icons
            data.subway = subway
            data.balcony = balcony
            data.publish = publish
            data.price = filter(str.isdigit,price).strip()
            data.price_way = price_way
            import pprint,json
            #print json.dumps(data.__dict__, ensure_ascii=False)            self.saveSql(data.__dict__)
            # t = (name,location,area,tier,usearea,traffic_distance,icons,','.join(subway),balcony,publish,''.join(price.split()),price_way)
            # self.dt[t] = None
            try:
                self.saveSql(data.__dict__)
            except Exception as e:
                log.error(e)



    #这里准备做第二张表格，里面是详细信息，声明其他类，有需求了在做。
    def getHomepage(self,url):
        html = self.getPageContent(self.url)
        pass

    def getAllUrl(self,content):
        resualt = {}
        #区域获取
        # ul = self.reSearch('<dl class="clearfix zIndex6">[\s\S]*?</dl>',content,0)
        # dlis = re.findall('<a.*?href="([\s\S]*?)".*?>([\s\S]*?)</a>',ul)
        # for li in dlis:
        #     resualt[formatUrl(li[0])] = li[1]
        ul_s = self.reSearch('<dl class="clearfix zIndex5">[\s\S]*?</dl>',content,0)
        subwaylis = re.findall('<a.*?href="([\s\S]*?)".*?>([\s\S]*?)</a>',ul_s)
        for li in subwaylis:
            resualt[formatUrl(li[0])] = li[1]
        return resualt

    def getPageNum(self,content):
        '''
        爬虫陷阱，无论拼接数值多大都会返回最后一页
        :param content:
        :return: pagenum
        '''
        nu = re.compile("<span>共(\d+?)页</span>")
        if nu:
            num = nu.search(content).group(1)
            if num.isdigit():
                return int(num)
        else:
            return 20

    def main(self,url,keyword,num=20):
        if not isinstance(num,int):
            num = 20
        if url == '':
            url = 'http://www.ziroom.com/z/nl/z3.html?qwd={keyword}'.format(keyword=keyword)
            content = self.getPageContent(url)
            num = self.getPageNum(content)
            urlList = self.getAllUrl(content)
            for url in urlList:
                keyword = urlList[url]
                if keyword == '全部':
                    continue
                print '------'
                print '%s start'%keyword
                time.sleep(random.random())
                for i in range(num):
                    url = url + "?p={page}".format(page=i)
                    self.getPage(url,keyword)
        else:
            self.getPage(url,keyword)
        # from crawler_project.utills.exalutils import writeXl
        # writeXl('ziru.xls',self.dt )


if __name__ == "__main__":
    url = 'http://www.ziroom.com/z/nl/z3.html?qwd=%E5%8C%97%E4%BA%AC&p=2'
    Ziru().main(url='',keyword='北京')

