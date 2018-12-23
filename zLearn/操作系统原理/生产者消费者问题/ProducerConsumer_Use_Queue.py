# 在原来使用list的位置，改为使用Queue实例（下称队列）。
# 这个队列有一个condition，它有自己的lock。如果你使用Queue，你不需要为condition和lock而烦恼。
# 生产者调用队列的put方法来插入数据。
# put()在插入数据前有一个获取lock的逻辑。
# 同时，put()也会检查队列是否已满。如果已满，它会在内部调用wait()，生产者开始等待。
# 消费者使用get方法。
# get()从队列中移出数据前会获取lock。
# get()会检查队列是否为空，如果为空，消费者进入等待状态。
# get()和put()都有适当的notify()。

from threading import Thread
import time
import random
from queue import Queue
que = Queue(10)


class ProducerThread(Thread):

    def run(self):
        nums = range(5)
        global que
        while True:
            num = random.choice(nums)
            que.put(num)
            print("Produced %d" % num)
            time.sleep(random.random())


class ConsumerThread(Thread):

    def run(self):
        global que
        while True:
            num = que.get()
            que.task_done()
            print("Consumed %d" % num)
            time.sleep(random.random())

ProducerThread().start()
ConsumerThread().start()
