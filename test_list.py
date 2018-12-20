# 定义 一般为相同数据类型和结构
import copy
my_list = ["zhangsan", "lisi", "xiaowu", "MIsi"]
tuple   = (1, "li", "lisi", 2)
dict    = {"name":"xiao","age":18, "city":"chongqing","height":167}

my_list.reverse()
my_list.append("add")
my_list.extend(["aa", "bb", "cc"])
list2 = [exp + "qqq" for exp in my_list if exp != "lisi"]
list3 = (exp + "qqq" for exp in my_list if exp != "lisi")
for next in list3:
    print(next)
list = list(dict)

dict_keys = dict.keys()
dict_vals = dict.values()
print(dict_keys)
print(dict_vals)


"""
list = my_list
my_list1 = [2, 3, 5, 1,100]
my_list2 = [2, [1,2], 5, 1,100, 1 ,(1, 2)]
my_list2c= my_list2[-2:2:-1] #[开始位置：结束位置；切片方向]
print(id(my_list2[1]), id(my_list2c[1]), my_list2c)
my_list1.sort()
print("list.sort 排序时无返回值列表直接被修改：",my_list1)
print("sorted(list) 排序时有返回值且key指定一个函数分别作用于列表每个元素：",sorted(my_list,key = str.lower))
print("可变对象浅拷贝：         ",id(my_list),id(copy.copy(my_list)))
print("可变对象切片时仍然为浅拷贝：",id(my_list),id(list),id((my_list)[:]))
print("[]访问指定index的值：",my_list1[2],"   ",id(my_list1))
my_list1[2] = 10000
print("  修改指定index的值：",my_list1[2],id(my_list1))
my_list1.append(99)
print("  append添加元素：",my_list1,id(my_list1))
print("  添加元素：insert（） append（） extend（）")
print("  删除元素：pop（[可选位置]） clear（） remove[内容] del 变量名[索引]")

list：数据结构
	-list1 = ['physics', 'chemistry', 1997, 2000]
	 形式 ：list[] 
	 元素类型： 它支持数字，字符串甚至可以包含列表（所谓嵌套）。

	-列表生成
			-语法：[exp for item in collection if codition]
			-list( tuple/str/set ) return a list
			-list(dict)    return keylist
			-range()(python2.x 中为列表 python3.x 中为可迭代对象)
	-访问	1，索引	返回一个元素
			2，切片 返回一个列表
	-追加	append（）方法 返回原列表
			s = [1, 2, 3]
			q = s.append(4)
			print(s, q) 
			>>[1, 2, 3, 4] None
	-删除	del
			del list[1]
			s = [1, 2, 3]
			s.pop(index) # 默认删除最后一个
	-修改	指定位置直接赋值
			s = [1, 2, 3]
			s[0] = [1,1]
	合并列表	+(list.extend()), *

	-切片	第一层深拷贝

	判断元素是否存在  3 in [1, 2, 3]

	-max(list) 方法返回列表元素中的最大值(数字为最小)
	-aList.reverse() 反向列表 无返回值
	-list.sort(cmp=None, key=None, reverse=False) 排序 无返回值
		-cmp 可选参数, 如果指定了该参数会使用该参数的方法进行排序。
		-key 具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序
			例如 def takeSecond(elem):
    				return elem[1]
			# 列表
			random = [(2, 2), (3, 4), (4, 1), (1, 3)]
			# 指定第二个元素排序
			random.sort(key=takeSecond)
"""