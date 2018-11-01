import requests
import random
import re
import time
from selenium import webdriver
from selenium.webdriver import ActionChains


href_list = []
user_agent_list = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16']
user_agent = random.choice(user_agent_list)
headers = {
        'User-Agent': user_agent,
        'Connection': 'keep - alive',
    }
Picreferer = {
    'User-Agent':user_agent,
    'Referer':'http://i.meizitu.net'
}
proxies={'https':'123.134.92.240:30956'}
def jiema(url):
    '''解码'''
    time.sleep(random.randint(1, 5))
    response = requests.get(url=url,headers=headers,proxies=proxies)
    # print(response.headers)
    response = response.text
    return response
def first_change(response):
    print(response)
    obj = re.findall(r'<a href="(http://www.mzitu.com/.*?)" target="_blank">', response)
    print(obj)
    for i in obj[1:]:
        print(i)
        response = jiema(i)
        second_change(response)
def second_change(response):
    driver = webdriver.Chrome("C:/Users/lenovo/AppData/Local/Google/Chrome/Application/chromedriver.exe")
    driver.get(response)
    time.sleep(5)
    driver.quit()


    # c = str(c)
    # try:
    #     obj = re.findall(r'<img src="(http://i.meizitu.net/.*?.jpg)".*/>',response)
    #     print(obj)
    #     obj = requests.get(url=obj,headers=Picreferer,proxies=proxies)
    #
    # except Exception as e:
    #     pass

def witer_url(obj,c):
    with open('./meizitu./%s.text' % c, 'wb+') as f:
        f.write(obj.content)
if __name__ == '__main__':
    url = 'http://www.mzitu.com/all/'
    # print(url)
    response = jiema(url)
    first_change(response)
    # witer_url()
    # print(href_list)
