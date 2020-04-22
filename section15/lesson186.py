"""
スレッドに渡す引数
"""


import logging
import threading
import time

"""
毎回これを書くのが面倒なので,loggingを使う
print(threading.currentThread().getName(), 'start')
"""

logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s'
)


def worker1():
    logging.debug('start')
    time.sleep(5)
    logging.debug('end')


def worker2(x, y=1):
    logging.debug('start')
    logging.debug(x)
    logging.debug(y)
    time.sleep(5)
    logging.debug('end')


if __name__ == "__main__":
    # name:スレッドの名前指定
    t1 = threading.Thread(name='rename worker1', target=worker1)
    # args(100, )←()の中が一つの場合は「,」をつけないとtupleにならないので注意
    t2 = threading.Thread(target=worker2, args=(100,), kwargs={'y': 200})
    t1.start()
    t2.start()
    print('started')
