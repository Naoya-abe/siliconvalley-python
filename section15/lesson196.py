"""
プロセス
並列処理ができる
threadと違い、処理一つ一つにメモリが当てられている
"""

# 一旦コードスタイルは無視
import logging
import multiprocessing
import time


logging.basicConfig(
    level=logging.DEBUG, format='%(processName)s: %(message)s'
)


def worker1(i):
    logging.debug('start')
    time.sleep(3)
    logging.debug(i)
    logging.debug('end')


def worker2(i):
    logging.debug('start')
    logging.debug(i)
    logging.debug('end')


if __name__ == "__main__":
    i = 10
    t1 = multiprocessing.Process(target=worker1, args=(i,))
    t1.daemon = True
    t2 = multiprocessing.Process(
        name='renamed worker2', target=worker2, args=(i,))
    t1.start()
    t2.start()

    # daemonを生かすなら
    t2.join()
    t1.join()
