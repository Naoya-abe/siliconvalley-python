"""
プロセス間通信に関して
パイプ
"""


import logging
import time
import multiprocessing


logging.basicConfig(
    level=logging.DEBUG, format='%(processName)s: %(message)s'
)


def f(conn):
    # parent_connからchild_connに値を渡す
    conn.send(['test'])
    time.sleep(5)
    conn.close()


if __name__ == "__main__":
    parent_conn, child_conn = multiprocessing.Pipe()
    p = multiprocessing.Process(target=f, args=(parent_conn, ))
    p.start()
    # joinがあればprocessが終わってから次の処理に進む
    # p.join()
    # .recv()でデータを共有する
    logging.debug(child_conn.recv())
