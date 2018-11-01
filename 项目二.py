import urllib.request
import urllib.parse
import json
import re
import random
import time

'''构建请求头'''
useragent_list=['Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50']
user_agent = random.choice(useragent_list)
headers = {
        'User-Agent': user_agent,
        'Connection': 'keep - alive',
    }
'''创建列表存储链接'''
second_href = []
a_href = []
c = 1
user_agent = random.choice(useragent_list)

def jiema(url):
    '''解码'''
    request = urllib.request.Request(url=url,headers=headers)
    try:
        response = urllib.request.urlopen(request).read().decode('utf-8')
        return response

    except:
        print( '网速问题')

def one_change(response):
    obj = re.findall(r'href="(.*?)" >',response)
    obj = str(obj)
    obj = re.findall(r'(https://hz.ke.com/ershoufang/\d+?.html)',obj)
    second_href.extend(obj)
def second_change():
    # print(second_href)
    for i in second_href:

        try:
            # print(i)
            response = jiema(i)
            # print(response)
            h = '''<span class="col-1">(.*?)</span>'''
            obj = re.findall(h, response)
            print(obj)
            with open('./House_property/fangwu.txt', 'a') as f:
                f.write("%s\n" % obj)


        except:
            continue
        # print(response)
        time.sleep(2)


if __name__ == '__main__':
    start = int(input('请输入起始页码：'))
    end = int(input('请输入结束页'))
    l = end-start+1
    for i in range(l):
        i = str(i)
        url = 'https://hz.ke.com/ershoufang/binjiang/pg%s/'%i
        response = jiema(url)
        # print(response)
        one_change(response)
        second_change()
    # print(a_href)