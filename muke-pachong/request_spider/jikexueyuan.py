#!/usr/bin/python
# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import requests
import  re
import string
import  sys
reload(sys)
#英文win7是gbk编码，需要强制转模块编码
sys.setdefaultencoding("utf-8")

class spider(object):
    def __init__(self):
        print "开始爬虫行动.."
        #获取网页源代码
    def getsource(self,url):
        html=requests.get(url)
        return html.text
    #生成网址列表
    def changepage(self,url,total_page):
        now_page=int(re.search('pageNum=(\d+)',url,re.S).group(1))
        page_group=[]
        for i in range(now_page,total_page+1):
            link=re.sub('pageNum=\d','pageNum=%s'%i,url,re.S)
            page_group.append(link)
        return page_group
    #获取单个网址下指定节点的内容
    def geteveryclass(self,source):
        everyclass=BeautifulSoup(source,"html.parser",from_encoding="utf-8").find("div",id="changeid").find_all("li")
        return everyclass
    #获取具体内容
    def getinfo(self,eachclass):
        info={}
        info['title']=eachclass.find("h2",class_="lesson-info-h2").find("a").get_text()
        info['content']=eachclass.find("div",class_="lesson-infor").find("p").get_text()
        timeandlevel=eachclass.find("div",class_="timeandicon").find_all("em")
        info['classtime']=timeandlevel[0].get_text()
        info["classlevel"]=timeandlevel[1].get_text()
        info["learnnum"]=timeandlevel[2].get_text()
        return info
   #新建一个文件来保存
    def saveinfo(self,classinfo):
        f=open('info.txt','a')
        for each in classinfo:
            f.writelines('********华丽风格线*********')
            f.writelines('title: '+each['title']+'\n')
            f.writelines('content: '+each['content']+'\n')
            f.writelines('classtime: '+each['classtime']+'\n')
            f.writelines('classlevel: '+each['classlevel']+'\n')
            f.writelines('learnnum: '+each['learnnum']+'\n')
        f.close()
#如果实在当前页面运行当前类时候就执行下面这段代码
if __name__=='__main__':
    classinfo=[]
    url="http://www.jikexueyuan.com/course/?pageNum=1"
    #新建爬虫类
    jikespider=spider()
    all_links=jikespider.changepage(url,20)
    for link in all_links:
        print "正在处理页面"+link
        html=jikespider.getsource(link)
        everyclass=jikespider.geteveryclass(html)
        for each in everyclass:
            info=jikespider.getinfo(each)
            classinfo.append(info)
    jikespider.saveinfo(classinfo)


