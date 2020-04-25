"""
プロセス間通信に関して
マルチスレッドの場合では、メモリを共有していたので
スムーズにデータのやりとりが出来ていたが
マルチプロセスではメモリを共有していないので、マルチスレッドとはデータの共有方法が異なる
"""


import logging
import threading
import time
import multiprocessing


logging.basicConfig(
    # level=logging.DEBUG, format='%(threadName)s: %(message)s'
    level=logging.DEBUG, format='%(processName)s: %(message)s'
)


def worker1(d, lock):
    with lock:
        i = d['x']
        time.sleep(2)
        d['x'] = i + 1
    logging.debug(d)


def worker2(d, lock):
    with lock:
        i = d['x']
        time.sleep(2)
        d['x'] = i + 1
    logging.debug(d)


if __name__ == "__main__":
    d = {'x': 0}
    lock = threading.Lock()

    # threadの場合
    # t1 = threading.Thread(target=worker1, args=(d, lock))
    # t2 = threading.Thread(target=worker2, args=(d, lock))

    # multiprocessの場合
    t1 = multiprocessing.Process(
        target=worker1, args=(d, lock))  # Process-1: {'x': 1}
    t2 = multiprocessing.Process(
        target=worker2, args=(d, lock))  # Process-2: {'x': 1}

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    logging.debug(d)  # MainProcess: {'x': 0}
