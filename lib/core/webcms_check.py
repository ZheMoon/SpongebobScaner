#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# __author__ = 'TomKing'

import json, os, sys, hashlib, threading, queue
from lib.core import Download

class webcms(object):
    """
    WebCMS指纹识别类
    """
    workQueue = queue.Queue()
    URL = ""
    threadNum = 0
    NotFound = True
    Downloader = Download.Downloader()
    result = ""

    def __init__(self, url, threadNum = 10):
        self.URL = url
        self.threadNum = threadNum
        filename = os.path.join(sys.path[0], 'fuzz', 'cms.json')
        with open(filename, encoding="utf-8") as f:
            webdata = json.load(f, encoding='utf-8')
            for i in webdata:
                self.workQueue.put(i)


    def getmd5(self, body):
        m2 = hashlib.md5()
        m2.update(body)
        return m2.hexdigest()


    def th_whatweb(self):
        if(self.workQueue.empty()):
            self.NotFound = False
            return False

        if(self.NotFound is False):
            return False

        cms = self.workQueue.get()
        _url = self.URL + cms['url']
        html = self.Downloader.get(_url)
        print("[whatweb log] : checking %s" % _url)
        if(html is None):
            return False
        if cms['re']:
            if(html.find(cms['re']) != -1):
                self.result = cms['name']
                self.NotFound = False
                return True

        else:
            md5 = self.getmd5(html)
            if(md5 == cms['md5']):
                self.result = cms['name']
                self.NotFound = False
                return True


    def run(self):
        while(self.NotFound):
            th = []
            for i in range(self.threadNum):
                t = threading.Thread(target=self.th_whatweb)
                t.start()
                th.append(t)
            for t in th:
                t.join()
        if(self.result):
            print("[webcms] : %s cms is %s" % (self.URL, self.result))
        else:
            print("[webcms] : %s cms NotFound!" % self.URL)
