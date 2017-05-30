#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from lib.core import Download, UrlManager
import threading
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from script import sqlcheck

class SpiderMain(object):
    """
        该类主要是：爬虫行为类
        用于页面爬取，链接获取等操作
    """
    def __init__(self, root, threadNum):
        self.urls = UrlManager.UrlManager()
        self.download = Download.Downloader()
        self.root = root
        self.threadNum = threadNum


    def _judge(self, domain, url):
        """
        判断是否是同一域名的链接
        :param domain: 域名
        :param url: 链接
        :return:
        """
        if url.find(domain) != -1:
            return True
        else:
            return False


    def _parse(self, page_url, content):
        """
        解析当前页面
        :param page_url: 当前页面链接
        :param content: 页面内容
        :return:
        """
        if content is None:
            return None
        soup = BeautifulSoup(content, "html.parser")
        _news = self._get_new_urls(page_url, soup)
        return _news


    def _get_new_urls(self, page_url, soup):
        """
        获取页面中所有的二级页面链接
        :param page_url: 当前页面链接
        :param soup: 文档对象
        :return:
        """
        new_urls = set()
        links = soup.find_all('a')
        for link in links:
            new_url = link.get('href')
            new_full_url = urljoin(page_url, new_url)
            if self._judge(self.root, new_full_url):
                new_urls.add(new_full_url)
        return new_urls

    def craw(self):
        """
        爬虫入口
        :return:
        """
        self.urls.add_new_url(self.root)
        while self.urls.has_new_url():
            _content = []
            th = []
            for i in list(range(self.threadNum)):
                if self.urls.has_new_url() is False:
                    break
                new_url = self.urls.get_new_url()
                # sql check
                try:
                    if (sqlcheck.sqlcheck(new_url)):
                        print("url:%s sqlcheck is valueable" % new_url)
                except:
                    pass
                print("crwa: %s" % new_url)
                t = threading.Thread(target=self.download.download, args=(new_url, _content))
                t.start()
                th.append(t)
            for t in th:
                t.join()
            for _str in _content:
                if _str is None:
                    continue
                new_urls = self._parse(new_url, _str['html'])
                self.urls.add_new_urls(new_urls)