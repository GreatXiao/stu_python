import  os
print(os.name)
print(os.uname()) # 查看操作系统
print(os.environ) # 查看环境变量
print(os.path.abspath(",")) # 查看当前文件绝对路径
# print(os.path.join("/home/xiao/Desktop/test_liao", "xiao"))
# os.mkdir("/home/xiao/Desktop/test_liao/xiao/li/wang") # 创建文件目录
# os.rmdir("/home/xiao/Desktop/test_liao/xiao/li/wang") # 删除文件目录
# os.path.join("/home/xiao/Desktop/test_liao", "wang")
my_dict = {"1":2, "3":4, "5":6}

print("字符串操作StringIO：")
from io import  StringIO
f = StringIO()
f.write("hello")
f.write("world")
print("getvalue()方法取值",f.getvalue())

f1 = StringIO("Hello!\nHi\nGood！")
s = f1.readlines()
for st in s:
    print(st.strip())
# while True:
#     s = f1.readline()
#     if s == "":
#         break
#     print(s.strip()) # strip()移除字符串两端空格
print("二进制操作StringIO：")
from io import BytesIO
f2 = BytesIO()
f2.write("中文".encode("utf-8"))
print(f2.getvalue())
