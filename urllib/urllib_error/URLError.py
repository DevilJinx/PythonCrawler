# -*- coding=utf-8 -*-
from urllib import request, error

'''URLError类来自urllib库的error模块，它继承自OSError类，是error异常模块的基类，由request模块产生的异常都可以通过捕获这个类来处理。
我们打开一个不存在的页面，照理来说应该会报错，但是这时我们捕获了URLError这个异常。
程序没有直接报错，而是输出Not Found，这样我们就可以避免程序异常终止，同时异常得到了有效处理。'''

try:
    response = request.urlopen('https://cuiqingcai.com/index.htm')
except error.URLError as e:
    print(e.reason)