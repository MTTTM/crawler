#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import   sys
import re
reload(sys)
sys.setdefaultencoding("gb18030")
type=sys.getfilesystemencoding()
#添加浏览器header，伪装成浏览器浏览
headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36"}
html=requests.get("http://jp.tingroom.com/yuedu/yd300p/",headers=headers)
html.encoding="utf-8"

#print html.text
title=re.findall('color:#666666;">(.*?)</span>',html.text,re.S)
for each in title:
    print each
print """
    ***
    ***
    ***
    ***
    ***


    """
chines=re.findall('color: #039;">(.*?)</a>',html.text,re.S)
for each in chines:
    print each