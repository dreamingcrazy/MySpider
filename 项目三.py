import urllib.request


headers={"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"}
url = 'http://www.baidu.com'
request = urllib.request.Request(url=url,headers=headers)
handler_obj = urllib.request.HTTPHandler()
opener = urllib.request.build_opener(handler_obj)
response = opener.open(request).read().decode('utf-8')
print(response)