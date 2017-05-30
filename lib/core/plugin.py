#!/usr/bin/env python3
# -8- coding:utf-8 -*-
# __author__ = 'Tomking'

import os
import sys

class spiderplus(object):
    """
    爬虫插件维护类
    """
    def __init__(self, plugin, disallow=[]):
        self.dir_exploit = []
        self.disallow = ['__init__']
        self.disallow.extend(disallow)
        self.plugin = os.getcwd() + '/' + plugin
        sys.path.append(self.plugin)


    def list_plugs(self):
        """
        获取所有可使用的插件
        :return:
        """
        def filter_func(file):
            if not file.endswith(".py"):
                return False
            for disfile in self.disallow:
                if disfile in file:
                    return False
            return True
        dir_exploit = filter(filter_func, os.listdir(self.plugin))
        return list(dir_exploit)


    def work(self, url, html):
        """
        运行插件
        :param url: 网页链接
        :param html: 网页源码
        :return:
        """
        for _plugs in self.list_plugs():
            try:
                m = __import__(_plugs.split('.')[0])
                spider = getattr(m, 'spider')
                p = spider()
                s = p.run(url, html)
            except Exception as e:
                print(e)


