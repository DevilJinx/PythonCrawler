# -*- coding=utf-8 -*-
from urllib.parse import urlunparse

'''URL的构造，为urlparse()的对立方法。这里参数data用了列表类型'''

data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
print(urlunparse(data))