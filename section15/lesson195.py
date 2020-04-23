"""
バリア
指定した数だけ異なるthreadの中で「barrier.wait()」が走らないと、それ以降の処理を実行しない
クライアントとサーバーの2つのthreadを立ち上げてから、今後の処理を行いたい場合に有効
"""


import logging
import threading
import time


logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s'
)


def worker1(barrier):
    r = barrier.wait()
    logging.debug('num={}'.format(r))
    while True:
        barrier.wait()
        logging.debug('start')
        time.sleep(2)
        logging.debug('end')


def worker2(barrier):
    r = barrier.wait()
    logging.debug('num={}'.format(r))
    while True:
        barrier.wait()
        logging.debug('start')
        time.sleep(2)
        logging.debug('end')


if __name__ == "__main__":
    barrier = threading.Barrier(2)
    t1 = threading.Thread(target=worker1, args=(barrier,))
    t2 = threading.Thread(target=worker2, args=(barrier,))
    t1.start()
    t2.start()
