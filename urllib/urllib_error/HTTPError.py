# -*- coding=utf-8 -*-
from urllib import request, error

'''HTTPError是URLError的子类，专门用来处理HTTP请求错误，比如认证请求失败等。它有如下3个属性：
code：返回HTTP状态码，比如404表示网页不存在，500表示服务器内部错误等。
reason：同父类一样，用于返回错误的原因。
headers：返回请求头。'''

try:
    response = request.urlopen('https://cuiqingcai.com/index.htm')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')


'''因为URLError是HTTPError的父类，所以可以先选择捕获子类的错误，再去捕获父类的错误，所以上述代码更好的写法如下：'''

try:
    response = request.urlopen('https://cuiqingcai.com/index.htm')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
except error.URLError as e:
    print(e.reason)
else:
    print('Request Successfully')