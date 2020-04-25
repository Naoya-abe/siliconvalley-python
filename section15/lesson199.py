"""
ワーカープロセスのプールとマップ
同時に走るプロセスの最大数を制御できる
複数プロセスを走らせたい時に、mapを使うとコードの行数を減らすことができる
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
    with multiprocessing.Pool(3) as p:
        # mapを使わない場合
        # p1 = p.apply_async(worker1, (100,))
        # p2 = p.apply_async(worker1, (200,))
        # logging.debug('execute apply')
        # logging.debug(p1.get())
        # logging.debug(p2.get())

        # mapを使う場合
        # この1行で上記の4行分のコードになる。（p1、p2関連）
        # 返り値はリスト
        # r = p.map(worker1, [100, 200])
        # logging.debug('execute')
        # logging.debug(r)

        # mapの返り値を待たないで次の行を実行したい場合
        # r = p.map_async(worker1, [100, 200])
        # logging.debug('execute')
        # logging.debug(r.get(timeout=1))

        # それぞれの値をfor文で処理したい場合
        r = p.imap(worker1, [100, 200])
        logging.debug('execute')
        for i in r:
            logging.debug(i)
