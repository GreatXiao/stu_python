# Numbers 数字  string 字符串   list 列表  tuple元祖  Dictionary(字典)

# 1、Numbers数字 string
# int = 1 (在-5～257之间，赋值时 他们属于同一块内存) 一个字节是8比特 11111111 = 255
# python3.5中 int理论是无限的
# 系统通过引用计数管理类存 创建、引用+1 删除时候-1
from sys import  getrefcount
a = 259999999999999999
b = 259999999999999999
c = "hello"
d = "hello"
# print(type(a))
print("计数器管理：",getrefcount(259999999999999999))
print("数字地址对比：",id(a)," ", id(b)," ",id(259999999999999999))
print("字符串地址对比:",id(c)," ", id(d)," ",id("hello"))
import sys
print(sys.getsizeof(int()))
print("---"*20)
print("---"*20)
# 2、列表,元祖、字典对比
e = (1, 2, 3)
f = (1, 2, 3)
list1 = [1, 2 ,3]
list2 = [1, 2 ,3]
print("元祖地址对比:",id(e)," ", id(f)," ",id((1, 2, 3)))
print("列表地址对比:",id(list1)," ", id(list2)," ",id([1, 2 ,3]))
