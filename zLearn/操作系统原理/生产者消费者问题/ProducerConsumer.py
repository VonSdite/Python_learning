# -*- coding: utf-8 -*-
# @Author   : Sdite
# @DateTime : 2017-06-15 10:36:27

from threading import *
import random
import time

condition = Condition()
lis = list()
MAX_NUM = 5


class Producer(Thread):
    """docstring for Producer"""

    def __init__(self):
        super(Producer, self).__init__()

    def run(self):
        global lis
        nums = range(5)
        while True:
            condition.acquire()
            if len(lis) == MAX_NUM:
                print("Room is full, producer is waiting")
                condition.wait()
                print("Consumer consums a produce, I produce a resourse again")
            resourse = random.choice(nums)
            lis.append(resourse)
            print("Produce resourse %d" % resourse)
            condition.notify()
            """ 
            notify源码解析： 
                __waiters = self.__waiters 
                waiters = __waiters[:n] # 获取等待队列中的n个等待锁 
                for waiter in waiters: 
                    waiter.release() # 释放Hider的等待锁 
                    try: 
                        __waiters.remove(waiter) 
                    except ValueError: 
                        pass 
            """
            condition.release()
            time.sleep(random.random())


class Consumer(Thread):
    """docstring for Consumer"""

    def __init__(self):
        super(Consumer, self).__init__()

    def run(self):
        global lis
        while True:
            condition.acquire()
            if not lis:
                print("There is no resourse")
                condition.wait()
                """ 
                wait()源码解析： 
                    waiter = _allocate_lock() 
                    # 创建一把等待锁，加入waiters队列，等待notify唤醒 
                    waiter.acquire()    # 获取锁 
                    self.__waiters.append(waiter) 
                    saved_state = self._release_save() 
                    # 释放condition.lock全局条件锁，以便其他等待线程执行 
                    if timeout is None: 
                        waiter.acquire() 
                        # 再次获取锁，因为已经锁定无法继续，等待notify执行release 
                """  
                # wait()释放对锁的占用，同时线程挂起在这里，直到被notify并重新占有锁。
                print("Producer produces a new resourse and I get it")
            resourse = lis.pop(0)
            print("Consum resourse %d" % resourse)
            condition.notify()
            condition.release()
            time.sleep(random.random())

Producer().start()
Consumer().start()
