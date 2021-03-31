from multiprocessing import Queue, Process


def consumer(name, q):
    """
    消费者方法
    """
    while True:
        msg = q.get()
        print('消费者{}: 消费了{}'.format(name, msg))


def producer(name, q):
    """
    生产者方法
    """
    for i in range(5):
        msg = '数字{}'.format(str(i))
        q.put(msg)
        print('生产者{}: 生产了{}'.format(name, msg))


if __name__ == '__main__':
    # 创建队列
    q = Queue()
    producer_1 = Process(target=producer, args=('小明', q))
    consumer_1 = Process(target=consumer, args=('小红', q))
    # 调用
    producer_1.start()
    consumer_1.start()

