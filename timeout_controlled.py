# -*- coding=utf-8 -*-
import socket
import urllib.request
import urllib.error

'''可以通过设置这个超时时间来控制一个网页如果长时间未响应，就跳过它的抓取。这可以利用try except语句来实现。这里我们请求了
http://httpbin.org/get测试链接，设置超时时间是0.1秒，然后捕获了URLError异常，接着判断异常是socket.timeout类型(意思就是超时异常)，
从而得出它确实是因为超时而报错，打印输出了TIME OUT'''
try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')