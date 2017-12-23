#!/usr/bin/env python
#coding:utf8

__Auther__ = "harry"
__Createtime__ = "2017/12/23 15:53"
__Version__ = 1

import os
import logging
import logging.config

from crawler_project.config.config import confPath
confPath = "/home/harry/ENV/crawler_project/config"

class logUtils(object):

    def __init__(self):
        conf = os.path.join(confPath,'logger.conf')
        print conf
        logging.config.fileConfig(conf)
        self.logger = logging.getLogger("root")

    def debug(self,arg):
        self.logger.debug(arg)

    def info(self,arg):
        self.logger.info(arg)

    def warn(self,arg):
        self.logger.warn(arg)

    def error(self,arg):
        self.logger.error(arg)

if __name__ == "__main__":
    logUtils().info('test')
