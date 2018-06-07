
print("""进程池！
#       """)
from multiprocessing import Pool
import  os, time, random
def long_time(name):
    print("run task %s (%s)"%(name, os.getpid()))
    print("记录开始时间！")
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print("task %s run %.2f seconds."%(name, (end-start)))
if __name__ == '__main__':
    print("Parent Process %s"% os.getpid())
    p = Pool(4)
    print("进程池参数为最大同时可执行的进程，Pool（）默认大小为cpu核数。")
    for i in range(5):
        p.apply_async(long_time,args = (i,))
    print("waiting for all subpricess done...")
    p.close()
    p.join()
    print("结束！")
