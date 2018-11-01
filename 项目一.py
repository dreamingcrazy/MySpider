# coding:utf-8
# 第一页： 'http://tieba.baidu.com/f?kw=%E6%A0%A1%E8%8A%B1&pn=0'
# 第二页：'http://tieba.baidu.com/f?kw=%E6%A0%A1%E8%8A%B1&pn=50'
#
# 100张图片
# 1、打开列表页
# 2、从列表页里面获取每一个帖子的链接
# 3、打开每一个帖子的链接，获取每一张图片的链接
# 4、打开图片的链接，下载图片

import urllib.request
# 用来构造请求，发送请求

import urllib.parse
# 进行url编码
# url1 = 'http://tieba.baidu.com/f?kw=%E6%A0%A1%E8%8A%B1&pn=0'
# url2 = 'http://tieba.baidu.com/f?kw=%E6%A0%A1%E8%8A%B1&pn=50'
import re

second_href = []



# 完成第一步，打开列表页

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
        'Connection': 'keep - alive',

    }




def create_request(url):
    '''这个函数用来构建请求对象'''


    request = urllib.request.Request(url=url,headers=headers)
    # print(request)
    return request

def send_request(request):
    '''这个函数用来发送请求'''
    response = urllib.request.urlopen(request).read().decode('gbk','ignore')
    # print(response)
    return response



def write_html_page(response,page_name):
    '''这个函数用来将爬取的网页写入文件'''
    with open(page_name,'w+') as file:
        file.write(response)

def tiqu_href(html):
    # print(html)
    obj = re.findall(r'<a rel="noreferrer" href="/p/\d+" title=".*" target="_blank" class="j_th_tit ">',html)
    obj = str(obj)
    obj = re.findall(r'href="(.*?)"',obj)

    # print(obj)
    second_href.extend(obj[2:])

def second_change():
    c=1
    for i in second_href:
    # i = second_href[1]
        url = 'https://tieba.baidu.com'+i
        # print(url)
        request = urllib.request.Request(url=url, headers=headers)
        response = urllib.request.urlopen(request).read().decode('gbk', 'ignore')
        # print(response)
        obj = re.findall(r'<img class="BDE_Image" src="(https://imgsa.baidu.com/.*?)"', response)
        print(obj)
        for n in obj:
            # print(n)
            request = urllib.request.Request(url=n, headers=headers)
            response = urllib.request.urlopen(request).read()
            with open('./meizi/%s.jpg'%c, 'wb+') as f:
                f.write(response)
            c += 1
    #<img class="BDE_Image" src=""
        # print(obj)
    # print(len(a))



if __name__ == '__main__':
    # tieba_name = input('请输入需要爬取的贴吧名字')
    # print(tieba_name)
    start = int(input('请输入起始页码：'))
    end = int(input('请输入结束页'))
    tieba_name = '妹子'
    # start = 1
    # end = 1

    # 将贴吧名字进行url编码
    tieba_name = urllib.parse.quote(tieba_name)

    for i in range(start,end+1):
        # 'http://tieba.baidu.com/f?' + tieba_name + '&pn=' + (n - 1) * 50


        url = 'http://tieba.baidu.com/f?kw=' + tieba_name + '&pn=' + str((i - 1) * 50)
        # print(url)
        request = create_request(url)
        response = send_request(request)
        tiqu_href(response)
        second_change()
        file_name = '这是第'+str(i) +'页的内容'
        write_html_page(response,file_name)

# print(second_href)