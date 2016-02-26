class UrlMangager(object):
    def __init__(self):
        self.new_urls=set()
        self.old_urls=set()
    def add_new_url(self,url):#添加新url
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
    def add_new_urls(self,urls): #批量添加url
        if urls is None or len(urls)==0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):#判断管理器中是否有新的带爬去的url
        return  len(self.new_urls)!=0
    def get_new_url(self):#获取新的url
       new_url=self.new_urls.pop()
       self.old_urls.add(new_url)


