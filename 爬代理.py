import requests
import random
import re
import time
href_list = []
user_agent_list = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16']
user_agent = random.choice(user_agent_list)
headers = {
        'User-Agent': user_agent,
        'Connection': 'keep - alive',
    }
proxies={'http':'61.135.217.7:80'}
def jiema(url):
    '''解码'''
    response = requests.get(url=url,headers=headers,proxies=proxies)
    response = response.text
    return response
def first_change(response):
    obj = re.findall('<td data-title="(.*?)">(.*?)</td>',response)
    href_list.extend(obj)
def witer_url():
    for obj in href_list:
        obj = str(obj)
        with open('./url/ip.txt', 'a') as f:
            f.write("%s\n"% obj)
if __name__ == '__main__':
    start = int(input('请输入起始页码：'))
    end = int(input('请输入结束页'))
    for h in range(start,end+1):
        h = str(h)
        url = 'https://www.kuaidaili.com/free/inha/%s'%h
        print(url)
        response = jiema(url)
        first_change(response)
        witer_url()
        print(href_list)
        time.sleep(random.randint(1,5))