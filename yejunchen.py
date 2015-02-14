#!/usr/bin/env python
# -*- coding: utf-8 -*-

" the help"
from __future__ import unicode_literals
from types import MethodType
from multiprocessing.managers import BaseManager
from collections import namedtuple
#from shutil import *
__author__ = "yejunchen"

import re
import sys
import math
import types
import base64
import logging
import pdb
import Image,ImageFilter
import codecs
import shutil
import threading
import functools
import random, time, Queue

#logging.basicConfig(level=logging.INFO)
print "hello yejunchen"

name = raw_input("hello,")
print name

#list / tuple
classmates = ["yejunchen","edward","Tracy"]

index = raw_input("the number you want to print:\n")

print classmates[int(index)]

apend_name = raw_input("append name:")
classmates.append(apend_name)

L = []
L.append(classmates)
print "len = %d\n" % (len(L))

t = ()
tt = (1, )
print "tt_len = %d t_len=%d\n" % (len(tt),len(t))

t = ('a','b',['A','B'])
t[2][0] = 'c'
t[2][1] = 'd'
print "t_len = %d %c\n" % (len(t),t[2][0])

#条件
age = 3
if age>=18:
	print "adult"
elif age >=6:
	print "teenager"
else:
	print "kid"

#循环
for names in classmates:
	print names,
print

sum = 0
for x in range(101):
	sum = sum + x
print "sum = %d\n" % (sum)

#dict(key-value) & set
di = {"yejunchen":1, "shiguan":2, "shouhu":333}
di[name] = 999
if name in di:
	print di[name]
print di.get("none this name",-1)
#key 不可变
#set 的key无重复，[]作为输入集
s = set([1,2,3,4])
s.add(5)
s.remove(1)

#函数
def nop():
	pass

def move(x, y, long, angle=0):
	nx = x + long*math.cos(angle)
	ny = y + long*math.sin(angle)
	return nx, ny
x, y = move(100,100,60, math.pi/6)
print x, y

#默认参数必须指向不变对象
def add_end(L = None):
	if L is None:
		L = []
	L.append(3)
	return L

Li = add_end()
Li = add_end(Li)

#可变参数, 接收tuple
def calc(*nums):
	sum = 0
	for x in nums:
		sum = sum + x
	return sum

#四种参数：必选、默认、可变、关键字（接收dict），必须按顺序
def funx(a, b, c=0, *args, **kw):
	print "a=%d b=%d c=%d"%(a, b, c),
	for str in args:
		print str,
	for keys in kw:
		print keys, kw[keys],
	return

args = (1,2,3,4)
kw = {"x":5, "y":6}
funx(7, 8, args=args, kw=kw)
funx(7, 8, 9, *args, **kw)
print
#尾递归调用:返回函数本身，无表达式
def facts(n, a=1, b=1):
	if b>n:
		return a
	return facts(n, a=a*b, b=b+1)

print facts(5)

#tuple和list，字符串等切片操作
#可迭代对象作用于for循环,for...in...
for i, value in enumerate(['a','b','c']):
	print i, value

#列表生成式可生成list
dd = {"x":"A", "y":"B", "z":"C"}
[k+"="+v for k, v in dd.iteritems()]

#生成器() or 函数yield中断
def fib(max):
	n, a, b = 0,0,1
	while n<max:
		yield b
		a, b = b, a+b
		n = n+1

for x in fib(6):
	print x

print


#module
def test():
	args = sys.argv
	if len(args)==1:
		print "hello."
	elif len(args)==2:
		print "hello,%s."%(args[1])
	else:
		print "too many."

if __name__ == "__main__":
	test()

#类
class Student(object):
	__slots__ = ("name", "age")
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def INF(self):
		print "name=%s, age=%d\n"%(self.name, self.age)

	def __str__(self):
		return "Student Class. %s."%(self.name)
	__repr__ = __str__

Lisa = Student("Lisa Walson", 20)
Lisa.INF()
print Lisa

def set_age(self, age):
	self.age = age

Student.set_age = MethodType(set_age, None, Student)
Lisa.set_age(5)
Lisa.INF()

print '\'xxx\' is unicode?', isinstance('xxx', unicode)
print 'u\'xxx\' is unicode?', isinstance(u'xxx', unicode)
print '\'xxx\' is str?', isinstance('xxx', str)
print 'b\'xxx\' is str?', isinstance(b'xxx', str)

#定制类：__iter__, __str__, __getitem__, __getattr__, __call__.
n = 0
logging.info("n=%d"%n)
#assert n!=0, "n is 0"
#pdb.set_trace()
#f  = open("mydict.txt", 'r')
#f.close()
with codecs.open("C:\data.txt", 'r') as f:
	for line in f.readlines():
		print(line.strip())

shutil.copyfile("C:\data.txt", "D:\pythoncode\copyf.txt")

Point = namedtuple("Point", ["x", "y"])
p = Point(1, 2)
print "Point x = %d, y = %d"%(p.x, p.y)

im = Image.open("heyi.jpg")
w, h = im.size
im.thumbnail((w//2, h//2))
im.save("heyi2.jpg", "jpeg")
im2 = im.filter(ImageFilter.BLUR)
im2.save("heyi3.jpg", "jpeg")