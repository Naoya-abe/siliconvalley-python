"""
ワーカープロセスのプールで非同期
同時に走るプロセスの最大数を制御できる
"""

import logging
import multiprocessing
import time


logging.basicConfig(
    level=logging.DEBUG, format='%(processName)s: %(message)s'
)


def worker1(i):
    logging.debug('start')
    time.sleep(3)
    logging.debug('end')
    return i


if __name__ == "__main__":
    # t1 = multiprocessing.Process(target=worker1, args=(i,))
    with multiprocessing.Pool(3) as p:
        p1 = p.apply_async(worker1, (100,))
        p2 = p.apply_async(worker1, (200,))
        logging.debug('execute apply')
        # timeout以上の時間がかかるようなら、エラーが返ってくる
        logging.debug(p1.get(timeout=1))
        logging.debug(p2.get())
