#!/usr/bin/python
# -*- coding: UTF-8 -*-
import  requests
html=requests.get("http://tieba.baidu.com/f?ie=utf-8&kw=python&fr=search")
print html.text