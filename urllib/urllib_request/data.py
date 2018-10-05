# -*- coding=utf-8 -*-
import urllib.parse
import urllib.request

'''data:附加数据
这里我们传递一个参数word，值是hello。它需要被转码成bytes(字节流)类型。其中转字节流采用了bytes()方法，该方法的第一个参数需要是str(字符
串)类型，需要用urllib.parse模块里的urlencode()方法来将参数字典转化为字符串；第二个参数指定编码格式，这里指定为utf-8'''

data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response.read())