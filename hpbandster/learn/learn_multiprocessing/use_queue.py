'''
展示如何使用 multiprocessing.Process 来进行单个进程的操作
'''

import multiprocessing as mp
import time, random, os


def func(x, dest_queue):  # 第一个是计算参数，第二个是要放入的queue
    print(os.getpid(), ' is working, spawned by ', os.getppid())
    dest_queue.put(x**2)
    return x ** 2


if __name__ == '__main__':

    q = mp.Queue()  # 为了进程间通信

    p = mp.Process(target=func, args=(11,q))  # Process的任务参数为target
    p.start()

    print('--sleep--')
    time.sleep(1)
    print('--wake up--')
    print('子进程放在Queue里的数值是', q.get(block=True, timeout=1))  # 阻塞主进程最多一秒，一秒内没返回结果就报超时
    print('q.empty() == ', q.empty(), '可以安全join了')  # 由于Queue是lazy的，所以一个进程put东西进去的时候并不是立刻完成
    # 经过上面的检验，进程put的工作确实进行了，而且也被安全的取出了，才可以终止这个进程
    '''
    Note multiprocessing uses the usual queue.Empty and queue.Full exceptions to signal a timeout. 
    They are not available in the multiprocessing namespace so you need to import them from queue.
    
    Note When an object is put on a queue, the object is pickled and a background thread later flushes the pickled data to an underlying pipe. 
    This has some consequences which are a little surprising, but should not cause any practical difficulties 
    – if they really bother you then you can instead use a queue created with a manager.
    **这里有个重点（用manager创建queue会好一些）**
    
    After putting an object on an empty queue there may be an infinitesimal delay before the queue’s empty() method returns False and get_nowait() can return without raising queue.Empty.
    If multiple processes are enqueuing objects, it is possible for the objects to be received at the other end out-of-order. However, objects enqueued by the same process will always be in the expected order with respect to each other.
    Warning: If a process is killed using Process.terminate() or os.kill() while it is trying to use a Queue, then the data in the queue is likely to become corrupted. This may cause any other process to get an exception when it tries to use the queue later on.
    Warning: As mentioned above, if a child process has put items on a queue (and it has not used JoinableQueue.cancel_join_thread), then that process will not terminate until all buffered items have been flushed to the pipe.
    This means that if you try joining that process you may get a deadlock unless you are sure that all items which have been put on the queue have been consumed. Similarly, if the child process is non-daemonic then the parent process may hang on exit when it tries to join all its non-daemonic children.

    Note that a queue created using a manager does not have this issue. See Programming guidelines.
    **这里有个重点（用manager创建queue会好一些）**
'''
    p.join()  # 回收子进程，
