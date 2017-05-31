#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# __author__ = 'TomKing'

import os
import sys
from lib.core.Download import Downloader

filename = os.path.join(sys.path[0], 'fuzz', 'web_shell.txt')
payload = []
pcount = 0
with open(filename) as f:
    for i in f:
        payload.append(i.strip())
        pcount += 1
        if pcount == 999:
            break

class spider(object):
    """
    webshell爆破
    """
    def run(self, url, html):
        if not url.endswith('.php'):
            return False
        print("[webshell check]", url)
        post_data = {}
        for _payload in payload:
            post_data[_payload] = "echo 'password is %s'" % _payload
            r = Downloader.post(url, post_data)
            if r:
                print("[webshell: %s]" % r)
                return True
        return False
