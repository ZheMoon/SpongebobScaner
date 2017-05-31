#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# __author__ = 'TomKing'

from lib.core import Download, common
import sys, os

payload = []
filename = os.path.join(sys.path[0], 'fuzz', 'xss_payload.txt')
with open(filename) as f:
    for i in f:
        payload.append(i.strip())

class spider(object):
    """
    xss测试模块
    """
    def run(self, url, html):
        if url is None:
            return False
        downloader = Download.Downloader()
        urls = common.urlsplit(url)

        if urls is None:
            return False

        for _urlp in urls:
            for _payload in payload:
                _url = _urlp.replace('my_Payload', _payload)
                print("[xss test]:", url)
                _str = downloader.get(_url)
                if _str is None:
                    return False
                if _str.find(_payload) != -1:
                    return True
        return False

