
print("装饰器：将函数名、参数 作为一个外层函数的参数调用 返回该函数")
"""
def log(test,func,*args,**kw):
    print("call[%s] %s()" % (test,func.__name__))
    return func(*args,**kw)
def now(x,y):
    print("now is me")
    return x+y
print(log("我是你爸爸",now,1,2))
print("将装饰器前加@ 放置定义处")
print("将装饰器前加@ 放置定义处 相当于执行 now2 = log（now2）")
"""
print("无参装饰器：")
def log(func):
        print("call %s()" % (func.__name__))
        return func
@log
def now():
    print("now is me")
now()

print("函数有参装饰器：")
def log1(func):
    def wrpp(*args, **kw):
        print("call %s()" % (func.__name__))
        return func(*args, **kw)
    return wrpp
@log1
def now1(x,y):
    print(x+y)
    print("now1 is me")
now1(1,2)
print(now1.__name__)
print("now1.name 改变 相当于执行@log时候：now1 = log1（now1）")
print("log1（now1）返回函数为wrpp")
