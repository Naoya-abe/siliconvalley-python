"""
プロセス間通信に関して
マネージャー
ValueとArrayよりもpythonっぽく簡単に記述できるが遅い
"""


import logging
import multiprocessing


logging.basicConfig(
    level=logging.DEBUG, format='%(processName)s: %(message)s'
)


def worker1(l, d, n):
    l.reverse()
    d['x'] += 1
    n.y += 1


if __name__ == "__main__":
    with multiprocessing.Manager() as manager:
        l = manager.list()
        d = manager.dict()
        n = manager.Namespace()

        l.append(1)
        l.append(2)
        l.append(3)
        d['x'] = 0
        n.y = 0

        p1 = multiprocessing.Process(target=worker1, args=(l, d, n))
        p1.start()
        p1.join()

        logging.debug(l)
        logging.debug(d)
        logging.debug(n)
