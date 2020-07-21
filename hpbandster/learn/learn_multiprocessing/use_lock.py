import multiprocessing as mp


def f(lock, x):
    lock.acquire()
    try:
        print('hello world', x)
    finally:
        lock.release()


if __name__ == '__main__':
    lock = mp.Lock()  # 创建一把锁

    for num in range(10):
        mp.Process(target=f, args=(lock, num)).start()  # 十个进程并行，但是都要用同一把锁
