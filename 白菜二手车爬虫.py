from bs4 import BeautifulSoup
import pymysql
import requests
import random
from lxml import etree
import time

"""数据库"""
db = pymysql.connect(host='localhost',user='zhanglin',password='123456',database='baicai_car',port=3306,charset='utf8')
cur = db.cursor()
"""请求设置"""

user_agent_list = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16']
user_agent = random.choice(user_agent_list)
proxies={'http':'117.191.11.105:8080'}
"""暂存列"""
brand_list = []
car_title_list = []
price_list = []
img_list = []
href_chack_list = []
make_car_year_list = []
driving_km_list = []
"""打开网页"""
def open_url(url):
    time.sleep(random.randint(1,5))
    response = requests.get(url=url,params=proxies).text
    return response
"""构造BS4对象"""
def make_bs4_obj(response):
    html_doc = BeautifulSoup(response, 'lxml')
    # print(html_doc)
    return html_doc
"""查找对象"""
def find_brand(html_doc):
    temporary = html_doc.select('font')
    for f in temporary:
        if f=='':
            brand_list.append('未找到')
        f = f.get_text()
        brand_list.append(f)
def find_car_title(html_doc):
    temporary = html_doc.select('h1')
    for f in temporary:
        if f=='':
            brand_list.append('未找到')
        f = f.get_text()
        car_title_list.append(f[3:])
def find_price(html_doc):
    temporary = html_doc.select('h3')
    for f in temporary[:-4]:
        if f=='':
            brand_list.append(0)
        f = f.get_text()
        f = f[:-1]
        price_list.append(f)
def find_img(html_doc):
    html_doc = etree.HTML(html_doc)
    temporary = html_doc.xpath("//div[4]/div[1]/ul/li/div[1]/a/img/@src")
    for f in temporary:
        if f=='':
            brand_list.append('未找到')
        f = str(f)
        img_list.append(f)
def find_href_chack(html_doc):
    temporary = html_doc.select('a[href]')
    for f in temporary:
        if f=='':
            brand_list.append('未找到')
        f = f['href']
        href_chack_list.append(f)
def find_make_car_year(html_doc):
    temporary = html_doc.select('div[class=info_param]')
    for f in temporary:
        if f=='':
            brand_list.append(0)
        f = f.select('span')
        f = f[0]
        f = str(f)
        f = f[6:-7]
        f = f[:-1]
        make_car_year_list.append(f)
def find_driving_km(html_doc):
    temporary = html_doc.select('div[class=info_param]')
    for f in temporary:
        if f=='':
            brand_list.append(0)
        f = f.select('span')
        f = f[1]
        f = str(f)
        f = f[6:-7]
        f = f[:-3]
        driving_km_list.append(f)
def insert_db():
    # print(brand_list)
    for i in range(len(brand_list)):
        try:
            sql = 'insert into car_list VALUES (0,%s,%s,%s,%s,%s,%s,%s)'
            cur.execute(sql,[brand_list[i], car_title_list[i], price_list[i], img_list[i], href_chack_list[i], make_car_year_list[i],driving_km_list[i]])
            db.commit()
        except Exception as e:
            print(e)



if __name__ == '__main__':
    start = int(input('请输入起始页码：'))
    end = int(input('请输入结束页'))
    for i in range(start, end + 1):
        i = str(i)
        url = 'https://hz.58.com/ershouche/pn%s/'%i
        response = open_url(url)
        html_doc = make_bs4_obj(response)
        find_brand(html_doc)
        find_car_title(html_doc)
        find_price(html_doc)
        find_img(response)
        find_href_chack(html_doc)
        find_make_car_year(html_doc)
        find_driving_km(html_doc)
        # insert_db()
        print(i)

