import threading
import multiprocessing

# 上記2つの方法よりもっと簡単に並列化が実現できる
# 単純な並列化ならこっちを使うs
import concurrent.futures
import logging
import time

logging.basicConfig(
    # level=logging.DEBUG, format='%(threadName)s: %(message)s'
    level=logging.DEBUG, format='%(processName)s: %(message)s'
)


def worker(x, y):
    logging.debug('start')
    r = x * y
    logging.debug(r)
    logging.debug('end')
    return r


def main():
    # multithread
    # with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        # f1 = executor.submit(worker, 2, 5)
        # f2 = executor.submit(worker, 4, 10)
        # logging.debug(f1.result())
        # logging.debug(f2.result())

        # process
        # args = [[2, 2], [5, 5]]
        # r = executor.map(worker, *args)
        # logging.debug(r)
        # logging.debug([i for i in r])

        # multiprocess
    with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:
        f1 = executor.submit(worker, 2, 5)
        f2 = executor.submit(worker, 4, 10)
        logging.debug(f1.result())
        logging.debug(f2.result())

        # process
        # args = [[2, 2], [5, 5]]
        # r = executor.map(worker, *args)
        # logging.debug(r)
        # logging.debug([i for i in r])


if __name__ == '__main__':
    main()
