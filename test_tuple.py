# 创建元祖 可存放字典、元祖
import copy
my_tuple = (1, "hello", [1, 2],("haha",1))
my_tuple1 = my_tuple[:]
print("打印元祖：",my_tuple)
print("遍历：",end="")
for t in my_tuple:
    print(t,end="-")
print("\nindex()获取元素索引：",my_tuple.index(1))
print("获取元素：",my_tuple[1][0])
print("+追加后地址对比",id(my_tuple), id(my_tuple + ("hehe",)))
print("切片时也为引用地址变化：",id(my_tuple), id(my_tuple1))
print("浅拷贝 = 赋值引用：   ",id(my_tuple),id(copy.copy(my_tuple)))
my_tuple[2][0] = 2
print("对其中字典修改过后：", my_tuple ,"地址不变", id(my_tuple))
a = 1, 2, 3
print("无括号时仍是tuple：",type(a))
# print("max（）取最大值：", max(my_tuple)) 类型不相同无法取最大值
def str_in(str1):
    str2 = str1
    print("tuple参数为引用传递：",id(str1))
st = my_tuple
str_in(st)
print("tuple实参传递：     ",id(st))
