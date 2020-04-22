"""
スレッドのLockとRLock

"""


import logging
import threading
import time


logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s'
)


def worker1(d, lock):
    logging.debug('start')
    # lock.acquire()  そこでlock.aquire()を使うと、lock.release()されるまで、他のthreadに邪魔されなくなる
    # i = d['x']
    # time.sleep(5)  しかし、このスレッドの処理がすごく長いと仮定すると
    # d['x'] = i + 1

    # lockはwithで書くことも可能
    with lock:
        i = d['x']  # iはここで0
        time.sleep(5)  # しかし、このスレッドの処理がすごく長いと仮定すると
        d['x'] = i + 1
        logging.debug(d)  # 出力：{'x': 1}
        with lock:
            j = d['x']
            d['x'] = j + 1
            logging.debug(d)
    logging.debug('end')


def worker2(d, lock):
    logging.debug('start')
    lock.acquire()
    i = d['x']
    d['x'] = i + 1
    logging.debug(d)  # 出力：{'x': 2} thread1の処理が長いと、出力が{'x': 1}になる
    lock.release()
    logging.debug('end')


if __name__ == "__main__":
    d = {'x': 0}
    # lock = threading.Lock()

    # lockをnestしたい場合にはRLockを使う
    lock = threading.RLock()
    t1 = threading.Thread(target=worker1, args=(d, lock))
    t2 = threading.Thread(target=worker2, args=(d, lock))
    t1.start()
    t2.start()
