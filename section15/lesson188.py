"""
生存中のThreadオブジェクト全てのリスト

"""


import logging
import threading
import time


logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s'
)


def worker1():
    logging.debug('start')
    time.sleep(3)
    logging.debug('end')


def worker2():
    logging.debug('start')
    time.sleep(2)
    logging.debug('end')


if __name__ == "__main__":
    # threading.enumerateを使わない場合
    # threads = [] threadを保存するための、配列が必要
    # for _ in range(5):
    #     t = threading.Thread(target=worker1)
    #     t.setDaemon(True)
    #     t.start()
    #     threads.append(t)
    # for thread in threads:
    #     thread.join()

    # threading.enumerateを使う場合
    for _ in range(5):
        t = threading.Thread(target=worker1)
        t.setDaemon(True)
        t.start()
    for thread in threading.enumerate():
        # threading.enumerate()にはmain_threadも含まれるので注意
        if thread is threading.currentThread():
            print(thread)
            continue
        thread.join()

    # t1 = threading.Thread(target=worker1)
    # t1.setDaemon(True)
    # t2 = threading.Thread(target=worker2)
    # t1.start()
    # t2.start()
    # print('started')
    # # デーモンスレッドを強制で終わらせたくない場合
    # t1.join()
    # # 実はt2.start()と書いた時点で、自動的にt2.join()も設定される
