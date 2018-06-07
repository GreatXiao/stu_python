# 定义string 为不可变类型
import copy
my_str = "agdag8qhgauuujhjyhuikjuuijhyuui"

print("取对应字母 index = 0",my_str[0])
print("切片：",my_str[:],"\n切片为引用：",id(my_str),id(my_str[:]))
print("浅拷贝 = 赋值：   ",id(my_str),id(copy.copy(my_str)))

# my_str[0]= "e" string 不支持赋值改变元素
print("s.xtrip 删除指定开头、结尾、中间指定序列：",my_str.strip("agd"))
my_str1 = my_str
print("赋值为引用）：",id(my_str),id(my_str1))

print("+链接新建对象）：",id(my_str),id(my_str + "wahaha"))
print("index()查找字符返回第一次出现的索引）：",my_str.index("gda"))
print("find()查找字符串：",my_str.find("gda"))
print("[：：-1]切片倒序：",my_str[::-1])

# 大小写转换 lower（）,upper(),swapcase()大小写互换
#          capitalize()(首字母大写)
def str_in(str1):
    str2 = str1
    str1 +="world"
    print("string参数传递：",id(str2),"形参发生变化后：",id(str1))
st = "hello"
str_in(st)
print("string作为实参：",id(st))
for s in st:
    print("元素遍历：",s, end="")
