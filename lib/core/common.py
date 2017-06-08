#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# __author__ = 'Tomking'

import socket
from urllib.parse import urlparse

def urlsplit(url):
    if url is None:
        return None
    domain = url.split('?')[0]
    _url = url.split('?')[-1]
    pararm = {}
    for val in _url.split('&'):
        pararm[val.split('=')[0]] = val.split('=')[-1]

    urls = []
    for val in pararm.values():
        new_url = domain + '?' + _url.replace(val,'my_Payload')
        urls.append(new_url)
    return urls


def gethostbyname(url):
    domain = urlparse(url)
    if domain.netloc is None:
        return None
    ip = socket.gethostbyname(domain.netloc)
    return ip
