# 1、定义
my_dict = {"name":"xiao","age":18, "city":"chongqing","height":167}
print("key取值：",my_dict["name"])
print("for遍历 为字典的key遍历：",end="")
for k in my_dict:
    print(k,end=",")
print("dict.values()返回一个值的列表：",my_dict.values())
print("dict.items()同时遍历key，Value:",end="")
for key, value in my_dict.items():
    print(key,"=", value,"\t",end = "")

