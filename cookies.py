# -*- coding=utf-8 -*-
import http.cookiejar, urllib.request

'''首先，我们必须声明一个CookieJar对象。接下来，就需要利用HTTPCookieProcessor来构建一个Handler，最后利用build_opener()方法构建出
Opener，执行open()函数即可。'''

cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
for item in cookie:
    print(item.name+"="+item.value)

# 输出为文本格式
'''CookieJar需要换成MozillaCookieJar，它在生成文件时会用到，是CookieJar的子类，可以用来处理Cookies和文件相关的事件，比如读取和保存
Cookies，可以将Cookies保存成Mozilla型浏览器的Cookies格式。'''
filename = 'cookies.txt'
# cookie = http.cookiejar.MozillaCookieJar(filename)
cookie = http.cookiejar.LWPCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)

'''另外，LWCookieJar同样可以读取和保存Cookies，但是保存的格式和MozillaCookieJar不一样，它会保存成libwww-perl(LWP)格式的Cookies文
件。要保存成LWP格式的Cookies文件，可以在声明时就改为：'''
# cookie = http.cookiejar.LWPCookieJar(filename)

'''生成Cookies文件，从文件中读取并利用(以LWPCookieJar为例)'''
cookie = http.cookiejar.LWPCookieJar()
cookie.load('cookies.txt', ignore_discard= True, ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
print(response.read().decode('utf-8'))