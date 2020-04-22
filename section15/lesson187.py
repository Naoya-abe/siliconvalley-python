"""
デーモンスレッド
現在は、スレッドの処理が全て完了したらプログラムが自動で終了する。
メインスレッドを含み、残っているスレッドがデーモンスレッドのみなら
デーモンスレッドを強制的に終了して、プログラムを終了する
"""


import logging
import threading
import time


logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s'
)


def worker1():
    logging.debug('start')
    time.sleep(5)
    logging.debug('end')


def worker2():
    logging.debug('start')
    time.sleep(2)
    logging.debug('end')


if __name__ == "__main__":
    t1 = threading.Thread(target=worker1)
    t1.setDaemon(True)
    t2 = threading.Thread(target=worker2)
    t1.start()
    t2.start()
    print('started')
    # デーモンスレッドを強制で終わらせたくない場合
    t1.join()
    # 実はt2.start()と書いた時点で、自動的にt2.join()も設定される
