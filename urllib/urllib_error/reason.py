# -*- coding=utf-8 -*-
import socket
import urllib.request
import urllib.error

'''reason属性返回的不是字符串，而是一个对象
用isinstance()方法来判断它的类型，作出更详细的异常判断'''

try:
    response = urllib.request.urlopen('https://www.baidu.com', timeout=0.01)
except urllib.error.URLError as e:
    print(type(e.reason))
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')