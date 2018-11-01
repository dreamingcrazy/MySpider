from selenium import webdriver
from selenium.webdriver import ActionChains

# 创建一个可操作对象
profile = webdriver.ChromeOptions("C:/Users/lenovo/AppData/Local/Google/Chrome/Application/chromedriver.exe")
profile.set_preference('network.proxy.type', 0)
profile.set_preference('network.proxy.http', '127.0.0.1')
profile.set_preference('network.proxy.http_port', 17890)  # int
profile.update_preferences()
driver = webdriver.Firefox(firefox_profile=profile)
# driver = webdriver.Chrome("C:/Users/lenovo/AppData/Local/Google/Chrome/Application/chromedriver.exe")

driver.get('https://www.baidu.com/')

# 获取返回的页面
response = driver.page_source
# print(type(response))

# # 1\找到元素所在的位置
find_el = driver.find_element_by_id('kw')



# ?2填写内容
find_el.send_keys('bilibili')
# 3发送请求
driver.find_element_by_id('su').click()
response_2 = driver.page_source

driver.find_element_by_xpath('//*[@id="1"]/h3/a[1]').click()
import time
time.sleep(12)
driver.quit()