#//div[@class='list-wrap']/p/span[1]/a/text() 户型
#//div[@class='list-item-intro']/a/@href  网址
#//div[@class='list-item-info']/span/text()  租金




from lxml import etree
import requests
import random
import time
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
proxies={'http':'117.191.11.105:8080'}
def paqu(i):

    url = 'https://m.ishangzu.com/hz/zufang/p' + str(i) + '/'
    time.sleep(random.randint(1, 5))
    response = requests.get(url=url,headers=headers,proxies=proxies,timeout=5).text
    html_doc = etree.HTML(response)
    return html_doc

def tiqu_one(html_doc):
    #地址
    address_list = html_doc.xpath("//div[@class='list-wrap']/p/span[1]/a/text()")
    #超链接
    href_list = html_doc.xpath("//div[@class='list-item-intro']/a/@href")
    #户型
    home_list = html_doc.xpath("//div[@class='list-wrap']/p/span[1]/a/text()")
    #租金
    money_list = html_doc.xpath("//div[@class='list-item-info']/span/text()")
    f = open('./House_property/aishangzu.csv','a+')
    try:
        for i in range(len(href_list)):
            each_obj = []
            each_obj.append(href_list[i])
            each_obj.append(home_list[i])
            each_obj.append(address_list[i])
            each_obj.append(money_list[i])
            print(each_obj)

            f.write(' '.join(each_obj))
            f.write('\n')
    except Exception as e:
        print("小错误")

    f.close()

if __name__ == '__main__':
    start = int(input('请输入起始页码：'))
    end = int(input('请输入结束页'))
    for i in range(start, end + 1):
        html_doc = paqu(i)
        tiqu_one(html_doc)




