"""
生存中のThreadオブジェクト全てのリスト

"""


import logging
import threading
import time


logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s'
)


def worker1(x, y=1):
    logging.debug('start')
    logging.debug(x)
    logging.debug(y)
    time.sleep(3)
    logging.debug('end')


def worker2():
    logging.debug('start')
    time.sleep(2)
    logging.debug('end')


if __name__ == "__main__":
    # Timerを使えば指定した秒数後にthreadを開始できる
    # 引数の渡し方は同じ
    t = threading.Timer(3, worker1, args=(10,), kwargs={'y': 100})
    t.start()
