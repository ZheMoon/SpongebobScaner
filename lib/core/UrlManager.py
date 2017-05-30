#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# __author__ = 'Tomking'


class UrlManager(object):
    """
        url管理器，主要维护两个set()
        第一个是未爬取的链接
        第二个是已经爬取的链接
    """
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()


    def add_new_url(self, url):
        """
        添加一条未扫描链接
        :param url: 链接
        :return:
        """
        if url is None:
            return None
        if ( url not in self.new_urls ) and ( url not in self.old_urls ):
            self.new_urls.add(url)


    def add_new_urls(self, urls):
        """
        添加多条未扫描链接
        :param urls: 链接
        :return:
        """
        if urls is None or len(urls) == 0:
            return None
        for url in urls:
            self.add_new_url(url)


    def has_new_url(self):
        """
        判断是否存在未扫描链接
        :return:
        """
        return len(self.new_urls) != 0


    def get_new_url(self):
        """
        获取一条未扫描链接
        :return:
        """
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url