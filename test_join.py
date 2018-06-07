# 1,基础语法
import  os
print(os.name)
print(os.uname()) # 查看操作系统
print(os.environ) # 查看环境变量
print("os.path.abspath 查看当前文件绝对路径:",os.path.abspath("test_join.py")) # 查看当前文件绝对路径
print("os.path.join 链接字符串：",os.path.join("/home/xiao/Desktop/stu_python笔记", "xiao"))
# os.mkdir("./lang") # 创建文件目录
# os.rmdir("/home/xiao/Desktop/test_liao/xiao/li/wang") # 删除文件目录
os.path.join("/home/xiao/Desktop/stu_python笔记", "wang")
# os.rename("", "") os.remove("")
print("列出文件目录下所有目录：",[x for x in os.listdir(".") if os.path.isdir(x)])
print("列出文件目录下所有py文件：",[x for x in os.listdir(".")
                        if os.path.isfile(x) and os.path.split(x)[1] == ".py"])
