'''
展示如何使用 multiprocessing.pool.Pool 作为进程池进行多进程并行
'''

import multiprocessing as mp
import os, time, random


def func(x):
    print(os.getpid(), ' is working, spawned by ', os.getppid())
    return x**2


if __name__ == '__main__':
    with mp.Pool(processes=4) as mypool:  # 开辟有4个进程的进程池

        ans = mypool.map(func=func, iterable=range(10))  # map是一种调用进程池的方式,用于iterable类对相结合使用
        print(type(ans), type(ans[0]), ans, '-'*20, sep='\n')

        res = mypool.apply_async(func=func, args=(20,))  # apply_async是一种并发调用进程池的方式，比较简练有效
        print(res.get(timeout=1), '-'*20, sep='\n')     # apply_async返回对象再调用get得到返回值
