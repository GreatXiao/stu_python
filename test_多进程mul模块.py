
from multiprocessing import Process
import os
print("""夸平台模块multiprocessing
      """)


def run(name):
    print("run child process%s(%s)"% (name, os.getpid()))


if __name__ == '__main__':
    print("父进程 %s"% os.getpid())
    print("# 实例化一个Process 接收两个参数（函数， 元祖（既该函数的参数））")
    p = Process(target=run,args = ("test",))
    print("# p.star开始运行run（）")
    print(2+2)
    p.start()
    print("# p.join保证子进程结速后再往下执行")
    p.join()
    print(2+2)

