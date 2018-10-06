# -*- coding=utf-8 -*-
from urllib.parse import urlsplit

'''这个方法不再单独解析params这一部分，只返回5个结果，上面例子中的params会合并到path中'''
result = urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
print(result)

'''以上代码返回结果是SplitResult，它其实也是一个元组类型，既可以用属性获取值，也可以用索引来获取'''
result = urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
print(result.scheme, result[0])