#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = "jc"

from wsgiref.simple_server import make_server

def application(environ, start_response):
	start_response("200 OK", [('Content-Type', 'text/html')])
	return "<h1> hello, %s!</h1>" % (environ['PATH_INFO'][1:] or 'web')

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('', 8000, application)
print "Serving HTTP on port 8000..."
# 开始监听HTTP请求:
httpd.serve_forever()

#入口是一个WSGI处理函数。HTTP请求的所有输入信息都可以通过environ获得
#HTTP响应的输出都可以通过start_response()加上函数返回值作为Body。