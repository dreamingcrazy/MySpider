import requests

headers={"User-Agent":"Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36"}
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

data = {

'i': '月亮',
'from': 'AUTO',
'to': 'AUTO',
'smartresult': 'dict',
'client': 'fanyideskweb',
'salt': 1540265025911,
'sign': '11e47488f2574a40b25a4a1435c9e699',
'doctype': 'json',
'version': 2.1,
'keyfrom': 'fanyi.web',
'action': 'FY_BY_REALTIME',
'typoResult': 'false'



}
proxies={'http':'61.135.217.7:80'}


response = requests.post(url=url,data=data,headers=headers,proxies=proxies)
print(response.cookies)
response = response.text

