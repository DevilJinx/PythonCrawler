# -*- coding = utf-8 -*-
import urllib.request

response = urllib.request.urlopen('https://www.python.org')

# 抓取整个网页代码
print(response.read().decode('utf-8'))
# 输出响应类型
print(type(response))
# 输出响应的状态码
print(response.status)
# 输出响应的头信息
print(response.getheaders())
# 输出通过调用getheader()方法并传递一个参数Server获取响应头中的Server值
print(response.getheader('Server'))