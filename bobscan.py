#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
Name:SpongebobScaner
Author: TomKing
Copyright (c) 2017
'''

import sys
from lib.core.Spider import SpiderMain
from lib.core import webcms_check, common, PortScan


def main():
    #root = "http://www.shiyanlou.com/"
    root = "http://ctf5.shiyanbar.com/423/web/?id=1"
    threadNum = 10
    ip = common.gethostbyname(root)
    print("IP:", ip)
    print("Start Port Scan:")
    pp = PortScan.PortScan(ip)
    pp.work()

    #webcms
    ww = webcms_check.webcms()
    ww.run()

    #spider
    sbs = SpiderMain(root, threadNum)
    sbs.craw()


if __name__ == '__main__':
    main()
