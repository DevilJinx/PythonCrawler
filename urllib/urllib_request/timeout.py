# -*- coding=utf-8 -*-
import urllib.request

'''timeout用于设置超时时间，单位为秒，意思就是如果请求超出设置的这个时间，还没有得到响应，就会抛出异常。如果不指定该参数，就会使用全局默认
时间。它支持HTTP、HTTPS、FTP请求'''

response = urllib.request.urlopen('http://httpbin.org/get', timeout=1)
print(response.read())