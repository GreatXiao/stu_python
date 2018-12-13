# 同步分支
from io import StringIO
f = StringIO() # 创建一个对象
f.write("hello") # 写入内存
print(f.getvalue()) # 获取内存中的数据

f1 = StringIO("     hello,word!") #初始化内存Stringio类
while True:
    s = f1.readline()
    if s == "":
        break
    print(s.strip())
