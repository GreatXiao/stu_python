# 定义 一般为相同数据类型和结构
import copy
my_list = ["zhangsan", "lisi", "xiaowu", "MIsi"]
my_list1 = [2, 3, 5, 1,100]
my_list1.sort()
print("list.sort 排序时无返回值列表直接被修改：",my_list1)
print("sorted(list) 排序时有返回值且key指定一个函数分别作用于列表每个元素：",sorted(my_list,key = str.lower))
print("可变对象浅拷贝：         ",id(my_list),id(copy.copy(my_list)))
print("可变对象切片时仍然为浅拷贝：",id(my_list),id((my_list)[:]))
print("[]访问指定index的值：",my_list1[2],"   ",id(my_list1))
my_list1[2] = 10000
print("  修改指定index的值：",my_list1[2],id(my_list1))
my_list1.append(99)
print("  append添加元素：",my_list1,id(my_list1))
