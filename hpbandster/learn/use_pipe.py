'''
Pipe 返回的是两个 connection类的对象，默认情况下pipe是双向的
多个进程同时 写pipe的同一端 / 读pipe的同一端 会出问题
其他情况下pipe是进程安全的
'''


import multiprocessing as mp


def func(conn):
    conn.send([42, None, 'hello'])
    conn.close()


if __name__ == '__main__':
    parent_conn, child_conn = mp.Pipe()
    p = mp.Process(target=func, args=(child_conn,))
    p.start()
    print(parent_conn.recv())   # prints "[42, None, 'hello']"
    p.join()
