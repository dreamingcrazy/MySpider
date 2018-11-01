import random
import time
import requests
from lxml import etree

user_agent_list = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16']
user_agent = random.choice(user_agent_list)
headers = {

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
data = {
    'district': 'c3243f2018413f06',
    'area': '6ca9fe5a544e3555',
    'location': '',
    'price': 'c3243f2018413f06',
    'region': 'ad5c2180af0dcb36',
    'blockName': '',
    'time': '6ca9fe5a544e3555',
    'houseType': '27d3af3bd45acf5e',
    'listingNo': '',
    'currentPage': '1',
}
proxies={'http':'117.191.11.105:8080'}
def paqu(i):

    url = 'https://m.ishangzu.com/hz/zufang/p' + str(i) + '/'
    time.sleep(random.randint(1, 5))
    response = requests.post(url=url,headers=headers,proxies=proxies,data=data,timeout=5).text
    html_doc = etree.HTML(response)