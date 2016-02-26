 #!/usr/bin/python
# -*- coding: UTF-8 -*-
from baike_spider import url_manger,html_downloader,html_parser,html_outputer
# Traceback (most recent call last):
#   File "D:/py/muke-pachong/baike_spider/spider_main.py", line 3, in <module>
#     from baike_spider import url_manger,html_downloader,html_parser,html_outputer
# ImportError: No module named baike_spider
class SpiderMain(object):
    def __init__(self):
        self.urls=url_manger.UrlMangager() #url管理器
        self.downloader=html_downloader.HtmlDwonloader()#下载器
        self.parser=html_parser.HtmlParser()#解析器
        self.outputer=html_outputer.HtmlOutputer()#输出器
    def craw(self,root_url):
        count=1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url(): #如果有新的url
            try:
                new_url=self.urls.get_new_url()#取出其中一个url
                print "craw %d : %s"%(count,new_url)
                html_cont=self.downloader.download(new_url)#下载网页
                new_urls,new_data=self.parser.parse(new_url,html_cont)#保存url和对应数据
                self.urls.add_new_url(new_urls)#将新的url补充到url、管理器
                self.outputer.collect_data(new_data)#同时进行数据的收集
                if count==1000:
                    break
                count=count+1
            except:
                print "craw failed"
        self.outputer.output_html()

if __name__=="__main__":
    root_url="http://baike.baidu.com/view/21087.htm"
    obj_spider=SpiderMain()
    obj_spider.craw(root_url)
