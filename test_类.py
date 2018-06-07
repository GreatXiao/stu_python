class student(): # class也是一种数据类型

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age # 修改
        return self.__age

s = student("miss", 25)
print("."*50)
print("实例化类的访问（鸭子类型）：")
print("name为共有可以外部访问：",s.name)
print("age 为私有不可以外部访问：,s.__age")
print("age 为私有通过get函数访问：",s.get_age())
print("age 为私有通过set函修改(可以通过if对传入值做检查)：",s.set_age(50))
print("."*50)
print("hasattr(obj, \"属性/方法\")--判断是否有该属性\n\
setattr(obj,属性,设置量)\n\
getattrr(obj,属性)--获取属性")
print(hasattr(s, "set_age"))
print("."*50)
print("增：")
