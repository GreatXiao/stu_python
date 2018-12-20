print("函数式编程：将函数作为参数传递，函数作为返回值。")
print("         尽量不要将内置函数名赋值给变量")


# 高阶函数：将函数作为参数进行传递 以下主要用于序列处理
# map/reduce处理 返回迭代器
# map（函数，序列）    序列： 将每一个元素作为参数传入函数
# reduce（函数，序列） 将前两个元素 作为参数传入函数的返回值 与下一个元素一起作为参数再次传递
# filter（函数，序列） 过滤序列 Ture删除
def _odd_iter():
    n = 1
    while True:
        n = n+2
        yield n
f = _odd_iter()
print(f.__next__())
print(next(f))

def _not_d(n):
    return lambda x:x%n>0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_d(n),it)


# sorted（序列，key=函数） 排序
# 先函数作用于每一个元素 进行对象排序
from collections import  Iterator
r = map(lambda x:x*x,(1, 2, 3))
print(isinstance(r,Iterator))
print(r)
