'''
展示 Rlock 的用法
Rlock可以被同一个进程连续多次 acquire，再被同一个进程多次 release 之后才能对其他进程开放
'''

import multiprocessing as mp
import os


def f(rlock, x):
    rlock.acquire()  # 两个参数 block和timeout，用于处理等待其他进程还锁
    print(os.getpid(), 'get first key')
    try:
        rlock.acquire()  # 同一个进程可以多次acquire同一把R锁
        print('get second key:, arg x = ', x)
    finally:
        print('return second key')
        rlock.release()
        print('return first key', '-'*20, sep='\n')
        rlock.release()


if __name__ == '__main__':
    lock = mp.RLock()  # 创建一把R锁

    for num in range(10):
        mp.Process(target=f, args=(lock, num)).start()  # 十个进程并行，但是都要用同一把锁
