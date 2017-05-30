#!/usr/bin/env python3
# __author__ = 'Tomking'

import re

class spider(object):
    """
    Email搜素模块
    """
    def run(self, url, html):
        pattern = re.compile(
            r"[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?"
        )
        email_list = re.findall(pattern, html)
        if email_list:
            print(email_list)
            return True
        return False
