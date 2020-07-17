'''
Manager起到服务器的作用，它 hold 一系列 python object
其他进程可以处理这里面的 object
有点C语言全局变量的感觉，进程间公用，比较方便
支持的对象类型：
list, dict, Namespace, Lock, RLock, Semaphore, BoundedSemaphore, Condition, Event, Barrier, Queue, Value and Array.
'''


import multiprocessing as mp


def f(d, l):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.reverse()


if __name__ == '__main__':
    with mp.Manager() as manager:
        d = manager.dict()
        l = manager.list(range(10))

        p = mp.Process(target=f, args=(d, l))
        p.start()
        p.join()

        print(d)  # manager有点C语言全局变量的感觉，进程间公用，比较方便，多进程共用时注意先后顺序和加锁
        print(l)
