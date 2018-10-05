# -*- coding=utf-8 -*-
import urllib.request

'''依然用urlopen()方法来发送这个请求，只不过这次该方法的参数不再是URL，而是一个Request类型的对象。通过构造这个数据结构，一方面我们可以将
请求独立成一个对象，另一方面可更加丰富和灵活地配置参数'''

request = urllib.request.Request('https://python.org')
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))