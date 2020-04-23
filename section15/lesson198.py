"""
ワーカープロセスのプールでブロック
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
        # マルチプロセスを走らせる前に確実に
        # 終わらせたい処理は.apply()を使う
        logging.debug(p.apply(worker1, (300,)))
        logging.debug('execute apply')
        p1 = p.apply_async(worker1, (100,))
        p2 = p.apply_async(worker1, (200,))
        logging.debug('execute apply')
        logging.debug(p1.get())
        logging.debug(p2.get())
