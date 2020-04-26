# 別のマシン上で走るプロセス間のネットワーク越しの共有
import queue
from multiprocessing.managers import BaseManager
# 裏ではsocket通信をしてくれている

queue = queue.Queue()


class QueueManager(BaseManager):
    pass


QueueManager.register(
    # client側で'get_queue'メソッドを使うことで
    # queueを呼び出すことが可能
    'get_queue', callable=lambda: queue
)

# server側の設定
manager = QueueManager(
    address=('127.0.0.1', 50000),
    # 認証で使う(byte型)
    authkey=b'abcdefg'
)
# serverの作成
server = manager.get_server()
# serverの起動
server.serve_forever()
