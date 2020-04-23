"""
キュー
スレッド間でデータの受け渡しが可能
"""


import logging
import queue
import threading
import time


logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s'
)


def worker1(queue):
    logging.debug('start')
    while(True):
        item = queue.get()
        if item is None:
            break
        logging.debug(item)
        queue.task_done()
    logging.debug('end')


def worker2(queue):
    logging.debug('start')
    logging.debug(queue.get())  # FIFO: First In First Out
    logging.debug(queue.get())  # queueがない時はqueueが追加されるまで、自動的に待つ
    logging.debug('end')


if __name__ == "__main__":
    # queue = queue.Queue()
    # # main threadで繰り返し数を指定して、他のthreadを動かしたい場合
    # for i in range(10):
    #     queue.put(i)
    # t1 = threading.Thread(target=worker1, args=(queue,))
    # # t2 = threading.Thread(target=worker2, args=(queue,))
    # t1.start()
    # # queueのtaskが完了したのか確認
    # logging.debug('tasks are not done')
    # queue.join()
    # logging.debug('tasks are done')
    # # t2.start()
    # queue.put(None)

    # 処理がめちゃくちゃ多い場合h
    queue = queue.Queue()
    for i in range(100000):
        queue.put(i)
    ts = []
    # threadを3つ走らせて処理を分割
    for _ in range(3):
        t = threading.Thread(target=worker1, args=(queue,))
        t.start()
        # 何個のthreadが走っているかを管理
        ts.append(t)
    logging.debug('tasks are not done')
    queue.join()
    logging.debug('tasks are done')

    # 走っているthread分Noneを渡す
    for _ in range(len(ts)):
        queue.put(None)
