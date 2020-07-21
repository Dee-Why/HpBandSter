'''
展示如何使用 multiprocessing.Process 来进行单个进程的操作
'''

import multiprocessing as mp
import time, random, os


def func(x):
    print(os.getpid(), ' is working, spawned by ', os.getppid())
    return x**2


if __name__ == '__main__':
    p = mp.Process(target=func, args=(11,))
    p.start()  # 子进程启动

    print('--sleep--')  # 这一行很快，会赶在子进程返回之前
    time.sleep(1)        # 这里可以看出来真的是两个进程并行的效果
    print('--wake up--')  # 这一行会落在后面

    p.join()  # 回收子进程
