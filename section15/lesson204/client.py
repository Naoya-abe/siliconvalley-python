from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass


QueueManager.register(
    # client側でもserver側と同じ名前で定義
    'get_queue'
)


# client側でも設定
manager = QueueManager(
    address=('127.0.0.1', 50000),
    authkey=b'abcdefg'
)

# serverとコネクト
manager.connect()

# queueの取り出し
queue = manager.get_queue()
queue.put('hello')
