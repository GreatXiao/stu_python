print("迭代Iteration实质：任何可以用For循环的对象。序列可迭代为充分不必要条件")
print("迭代:就是单向、逐个访问容器中元素的行为。 V")
print("迭代器:数据用到时候再生成，可以被next（）调用并且不断返回下一个值的对象。一个把不同数据结构在迭代实现方法隐藏的工具、\n\
      被next（）作用不断返回下一值，直到抛出错误Stopiteration。计算时候是惰性的，需要返回时候才计算")
from collections import  Iterator
print("列表转化成迭代器：        isinstance((x for x in range(10)),Iterator)",isinstance((x for x in range(10)),Iterator))
print("列表、tuple...不是迭代器：isinstance([x for x in range(10)],Iterator)",isinstance([x for x in range(10)],Iterator))
print("迭代器的使用： 1、内置iter（容器）返回一个迭代器\n\
                    2、调用迭代器的next（）每次调用得到一个元素。'")

print("__"*50)
print("列表生成式。。。。。。。。。。。。。。")
list1 = list(range(10))# 调用list（创建列表）
list2 = [x for x in range(10) if x%2 ==0] #列表生成公式 带判断
list3 = [m+n for m in "ABC" for n in "XYZ"] # 生成2^3个元素列表
print("",list1,"\n",list2,"\n",list3)



print("__"*50)
print("生成器。。。。。。。。。。。。。。")
print("[]变为（）则转化为生成器：它是迭代器实现的转化")
print("生成器实质： 通过return 更换成 yield 函数执行调用next（）调用一次执行到yield则停止")
def yrange():
     n = 10
     while True:
        if n>0:
            yield n
            n = n-1
        else:
            break
f = yrange()

print(next(f))
print(next(f))
print(next(f))


