'''
使用 Value 或是 Array 提供了一种进程间共享内存的方式
虽然这种做法非常不推荐，但还是要了解一下
注意这里需要指明变量类型，有些 C 的风格
'''

import multiprocessing as mp


def f(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]


if __name__ == '__main__':
    num = mp.Value('d', 0.0)   # d means double (C style)
    arr = mp.Array('i', range(10))  # i means int (C style)

    p = mp.Process(target=f, args=(num, arr))
    p.start()
    p.join()

    print(num.value)  # Value对象调用value变量
    print(arr[:])  # Array对象使用重载好的[]即可
