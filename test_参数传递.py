def f1(a, b, *args, **kw):
    print("a:", a,"b:", b,"args:", args,"kw", kw)
# f1(1) 运行错误必选参数不能省略


num = (100,11,22)
print("参数传递时会自动对带*/**的变量进行拆包：\n后面再对应位置参数进行传递：")
f1(*num,name=99) # *和**默认均为空


def f2(*,city, job):
    print(city,job)


print("关键字参数只允许传递关键值，且必须指定值与位置参数相区别：")
f2(city="nanjing", job="xuesheng")
