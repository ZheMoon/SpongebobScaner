#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
Name:SpongebobScaner
Author: TomKing
Copyright (c) 2017
'''

import sys
from lib.core.Spider import SpiderMain


def main():
    root = "http://ctf5.shiyanbar.com/423/web/?id=1%29%28%22%27"
    threadNum = 10
    #spider
    sbs = SpiderMain(root, threadNum)
    sbs.craw()


if __name__ == '__main__':
    main()
