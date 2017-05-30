#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests

class Downloader(object):
    """
        该类主要处理http请求以及页面获取
    """
    def get(self, url):
        """
        GET请求
        :param url: 链接
        :return:
        """
        r = requests.get(url, timeout = 10)
        if r.status_code != 200:
            return None
        _str = r.text
        return _str


    def post(self, url, data):
        """
        POST请求
        :param url: 链接
        :param data: 发送数据
        :return:
        """
        r = requests.post(url, data)
        _str = r.text
        return _str


    def download(self, url, htmls):
        """
        获取页面信息
        :param url: 链接
        :param htmls:数据保存字典
        :return:
        """
        if url is None:
            return None
        _str = {}
        _str['url'] = url
        try:
            html = self.get(url)
            if html is None:
                return None
            _str['html'] = html
        except Exception as e:
            return None
        htmls.append(_str)