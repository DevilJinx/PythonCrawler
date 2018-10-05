# -*- coding=utf-8 -*-
from urllib.parse import urlparse

# 利用urlparse()方法进行了一个URL的解析。首先，输出了解析结果的类型，然后将结果也输出出来。
result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result), result)

'''urlparse()的API用法：urllib.parse.urlparse(urlstring, scheme='', allow_fragment=True)，共有三个参数：
urlstring：这是必填项，即待解析的URL。
scheme：它是默认的协议(比如http或https等)。假如这个链接没有带协议信息，会将这个作为默认的协议。'''
result = urlparse('www.baidu.com/index.html;user?id=5#comment', scheme='https')
print(result)

# scheme参数只有在URL中不包含scheme信息时才生效。如果URL中有scheme信息，就会返回解析出的scheme。带上scheme时如下：
result = urlparse('http://www.baidu.com/index.html;user?id=5#comment', scheme='https')
print(result)

'''allow_fragments：即是否忽略fragment。如果它被设置为False，fragment部分就会被忽略，它会被解析为path、parameters或者query的一部
分，而fragment部分为空。'''
result = urlparse('http://www.baidu.com/index.html;user?id=5#comment', allow_fragments=False)
print(result)

'''如果URL中不包含params和query'''
result = urlparse('http://www.baidu.com/index.html#comment', allow_fragments=False)
print(result)

'''返回结果ParseResult实际上是一个元组，我们可以用索引顺序来获取，也可以用属性名获取'''
result = urlparse('http://www.baidu.com/index.html#comment', allow_fragments=False)
print(result.scheme, result[0], result.netloc, result[1], sep='\n')