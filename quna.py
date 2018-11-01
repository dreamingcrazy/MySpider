#coding:utf-8
import requests
from lxml import etree
import random
import time
from selenium import webdriver
import threading
#线程安全
import queue
import re


#//ul[@class='b_strategy_list ']/li/h2/a 一级页面链接标题
class QUNAAPP():
    def __init__(self):
        """url构造"""
        user_agent_list = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16']
        user_agent = random.choice(user_agent_list)
        self.headers = {

                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                    'Accept-Encoding': 'gzip, deflate, sdch',
                    'Accept-Language': 'zh-CN,zh;q=0.8',
                    'Cache-Control': 'max-age=0',
                    'Connection': 'keep-alive',
                    'Cookie': 'isz_city=www; isz_uid=0aaf608b-e1dc-4d75-9926-6527f44bd1c8; Hm_lvt_2d1fb77e9aeb419bd6ce2ed0ad9592af=1538022510; Hm_lvt_95b48bca16692265c14e9a74c0d0f810=1538022510; XSRF-TOKEN=eyJpdiI6InhpeERKVzdOSXk3bE4yNVNDZjFhRkE9PSIsInZhbHVlIjoiNm4rM1Y2MGdoQk5QSUNJdzZWMlBmZWxwS2l5aGRmMTVlZEZRSHRXV1JXaE9pNDhrM1BHTkRGTFh0MHByWFN0VER1RnJkaUl5bGlKYWxhbHJFTWc2XC9RPT0iLCJtYWMiOiI1ZTZkZmRiZTNhOWEwNTFjZjI2NmRlMzI2YjQxYThhYjk1ZjUxZGNhZTc0NDIyNTc4Zjk5YWU1MTQzZDU0NTVlIn0%3D; isz_session=eyJpdiI6Ik5WcWtlTEZwWkRjVWd0cU5zbnJvWVE9PSIsInZhbHVlIjoiRWwzbnpPK0tFeVpRbkFHTzh4Z2J0YlNLSFNxVGcwZTlsYkJpUEIxbUg4bkdkWit6ZnJtVFo2dlVJV1U3d0hWaFwvZCttOGV2bVRSWU1IM3Nsdm1hZlNBPT0iLCJtYWMiOiI3YzkyNGY3NGU2ZjliMmI2NDY0Y2FmMDYzZTVlMTdmODIxNWFlOGVhNWQzMWYxMzFhN2IxNGI1ZTI0NGM4NTNjIn0%3D; Hm_lpvt_2d1fb77e9aeb419bd6ce2ed0ad9592af=1538022528; Hm_lpvt_95b48bca16692265c14e9a74c0d0f810=1538022528',
                    'Referer': 'https://www.ishangzu.com/zufang/p2',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': user_agent,
                }
        self.url_list = []
        self.proxies={'http':'117.191.11.105:8080'}
        self.data_queue = queue.Queue()


    """打开页面"""
    def open_url(self,url):

        time.sleep(random.randint(1, 5))
        response = requests.get(url=url,headers=self.headers,proxies=self.proxies,timeout=5).text
        # print(response)
        html_doc = etree.HTML(response)
        return html_doc
    def first_find(self,html_doc):
        biaoti = html_doc.xpath("//ul[@class='b_strategy_list ']/li/h2/a/text()")
        lianjie = html_doc.xpath("//ul[@class='b_strategy_list ']/li/h2/a/@href")
        c=1
        for i in lianjie:
            url = 'http://travel.qunar.com'+i+'/'
            print(url)
            second_url = self.open_url(url)
            self.second_find(second_url,c)
            time.sleep(random.randint(1,10))
            c+=1
    def second_find(self,second_url,c):
        neirong = second_url.xpath("//div[@class='text js_memo_node']/p/text()|//h4/dl/dt/div[2]/text()|//div[1]/h5/div[1]/a/text()|//div[@class='b_poi_title_box']/text()|//dl[@class='js_memo_node']/dt/img/@data-original")
        for i in neirong:
            d=1
            if re.findall(r"https://.*",i)==1:
                i = requests.get(url=i,headers=self.headers,proxies=self.proxies,timeout=5).content
                d = str(d)
                self.witer_wb(i,c,d)
            else:
                i=str(i)
                print(type(i))
                print(i)
                self.witer(i,c)
            d+=1

    def witer(self,neirong,c):
        with open('./quna/%s.doc' % c, 'a+',encoding='utf-8') as f:
            f.write(neirong)
    def witer_wb(self,neirong,c,d):
        with open('./quna/%s.doc/%s.jpg'%(c,d),'ab+') as f:
            f.write(neirong)
    def start_work(self,url):
        html_doc = self.open_url(url)
        self.first_find(html_doc)


    def start(self):
        thread_list = []
        start = int(input('请输入起始页码：'))
        end = int(input('请输入结束页'))
        for i in range(start, end + 1):
            url = 'http://travel.qunar.com/travelbook/list.htm?page='+str(i)+'&order=hot_heat'
            self.url_list.append(url)
        for url in self.url_list:
            thread = threading.Thread(target=self.start_work,args=(url,))
            thread.start()
            thread_list.append(thread)

        # 让主线程等待子线程执行完成之后,再继续执行
        for thread in thread_list:
            thread.join()

        while not self.data_queue.empty():
            print(self.data_queue.get())
if __name__ == '__main__':
    start = time.time()
    dbs = QUNAAPP()
    dbs.start()
    print(time.time() - start)