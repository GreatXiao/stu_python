print("""
# N/L系统下 运用os 模块调用fork
# 每次调用fork（）返回两次。自动复制一份进程 然后分别在父、子进程返回: 子进程永远返回0，父返回子Id
# 子.getppid()拿到父id
# 对os.fock()进行n次循环的时候创建2^1+2^2.....+2^n
      """)
import os

print("process(%s) start..." % os.getpid())
pid = os.fork()
if pid==0:
    print("child process(%s) and parent is %s" % (os.getpid(), os.getppid()))
else:
    print("(%s) just created a child process (%s)" % (os.getpid(),pid))
# print("子进程 nslookuo www.*********")
# import  subprocess
# r = subprocess.call(["nslookup", "www.python.org"])
# print("Exit code",r)
