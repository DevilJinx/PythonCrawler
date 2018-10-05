# -*- coding=utf-8 -*-
from urllib import request, parse

'''通过4个参数构造了一个请求，其中url即请求URL，headers中指定了User-Agent和Host，参数data用urlopen()和bytes()方法转成字节流。另外，
指定了请求方式为POST'''

url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'httpbin.org'
}
dict = {
    'name': 'Germey'
}
data = bytes(parse.urlencode(dict), encoding='utf8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))