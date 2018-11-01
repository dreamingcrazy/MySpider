# coding:utf-8
import urllib.request


def main():
    # 构造REQUEST请求
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Mobile Safari/537.36',
        'Connection': 'keep - alive',

    }

    request_obj = urllib.request.Request(url='http://www.taobao.com/', headers=headers)

    # 获取请求头
    user_agent = request_obj.get_header('User-agent')
    print(user_agent)

    # 获取connect

    conect = request_obj.get_header('Connection')
    print(conect)

    response = urllib.request.urlopen(request_obj)
    # 返回的是一个相应对象

    response = response.read()
    # 获取html的内容，read可以获取文件所有的内容
    return response


if __name__ == '__main__':
    main()