import os
import requests
from lxml import etree
import time
import random
from selenium import webdriver
import threading
#线程安全
import queue


# 将Chrome设置成不加载图片的无界面运行状态
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36")
chrome_options.add_argument('--proxy-server=http://117.191.11.105:8080')
chrome_path = 'C:/Users/lenovo/AppData/Local/Google/Chrome/Application/chromedriver.exe'

# 设置图片存储路径
PICTURES_PATH = os.path.join(os.getcwd(), 'pictures/')

# 设置headers
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/65.0.3325.181 Safari/537.36',
    'Referer': "http://www.mmjpg.com"
}


class Spider(object):
    def __init__(self):
        self.page_urls = []
        self.girl_urls = []
        self.girl_name = ''
        self.pic_urls = []

# 获取页面url的方法
    def get_page_urls(self):
        start = int(input('请输入起始页码：'))
        end = int(input('请输入结束页'))
        for i in range(start, end + 1):
            i = str(i)
            page_url = 'http://www.mmjpg.com/home/' + i
            self.page_urls.append(page_url)


# 获取妹子的url的方法
    def get_girl_urls(self):
        for page_url in self.page_urls:
            html = requests.get(page_url).content
            selector = etree.HTML(html)
            self.girl_urls += (selector.xpath('//span[@class="title"]/a/@href'))

# 获取图片的url的方法
    def get_pic_urls(self):
        driver = webdriver.Chrome(chrome_path, chrome_options=chrome_options)
        for girl_url in self.girl_urls:
            driver.get(girl_url)
            time.sleep(random.randint(1,5))
            driver.find_element_by_xpath('//em[@class="ch all"]').click()
            time.sleep(random.randint(1, 5))
            html = driver.page_source
            selector = etree.HTML(html)
            self.girl_name = selector.xpath('//div[@class="article"]/h2/text()')[0]
            self.pic_urls = selector.xpath('//div[@id="content"]/img/@data-img')
            try:
                a = self.download_pic()
                if a==1:
                    continue
            except Exception as e:
                print("{}保存失败".format(self.girl_name) + str(e))
        driver.quit()

# 下载图片的方法
    def download_pic(self):
        try:
            os.mkdir(PICTURES_PATH)
        except:
            pass

        girl_path = PICTURES_PATH + self.girl_name
        try:
            os.mkdir(girl_path)
        except Exception as e:
            print("{}已存在".format(self.girl_name))
            return 1
        img_name = 0
        for pic_url in self.pic_urls:
            img_name += 1
            img_data = requests.get(pic_url, headers=headers)
            pic_path = girl_path + '/' + str(img_name)+'.jpg'
            if os.path.isfile(pic_path):
                print("{}第{}张已存在".format(self.girl_name, img_name))
                pass
            else:
                with open(pic_path, 'wb')as f:
                    f.write(img_data.content)
                    print("正在保存{}第{}张".format(self.girl_name, img_name))
                    f.close()
        return

# 爬虫的启动方法，按照爬虫逻辑依次调用方法
    def start(self):
        self.get_page_urls()
        self.get_girl_urls()
        self.get_pic_urls()


# main函数
if __name__ == '__main__':

        mmjpg_spider = Spider()
        mmjpg_spider.start()