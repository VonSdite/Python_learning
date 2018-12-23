# -*- coding: utf-8 -*-
# @Author   : Sdite
# @DateTime : 2017-06-15 10:36:43

# 具体学习用另一个代码
# 这个代码是当没有资源的时候跳过，资源满了也跳过
from threading import *
import random
import time

lock = Lock()
lis = list()
count = 0
MAX_NUM = 5


class Producer(Thread):
    """docstring for Producer"""

    def __init__(self):
        super(Producer, self).__init__()

    def run(self):
        global lis, count, MAX_NUM
        nums = range(5)
        while True:
            lock.acquire()
            if count == MAX_NUM:
                lock.release()
            else:
                resourse = random.choice(nums)
                lis.append(resourse)
                print("Produce resourse %d" % resourse)
                count += 1
                lock.release()
            time.sleep(random.random())


class Consumer(Thread):
    """docstring for Consumer"""

    def __init__(self):
        super(Consumer, self).__init__()

    def run(self):
        global lis, count
        while True:
            lock.acquire()
            if count == 0:
                print("There is no resourse")
                lock.release()
            else:
                resourse = lis.pop(0)
                print("Consum resourse %d" % resourse)
                count -= 1
                lock.release()
            time.sleep(random.random())


Producer().start()
Consumer().start()
