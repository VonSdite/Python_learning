#-*- coding:utf-8 -*-

import threading
from time import sleep
import os
import random

# 设置为2更容易重现死锁
numPhilosophers = numForks = 2


class Waiter:

    def __init__(self):
        self.forks = [Fork(idx) for idx in range(numForks)]
        # 最开始餐叉还没有被分配给任何人，所以全部 False
        self.forks_using = [False] * numForks

    # 如果哲学家的左右餐叉都是空闲状态，就为这位哲学家服务提供餐叉
    def serve(self, philor):
        if not self.forks_using[philor.leftFork.index] and not self.forks_using[philor.rightFork.index]:
            self.forks_using[philor.leftFork.index] = True
            self.forks_using[philor.rightFork.index] = True
            self.forks[philor.leftFork.index].pickup()
            self.forks[philor.rightFork.index].pickup()
            return True
        else:
            return False

    # 哲学家用餐完毕后，清理并回收餐叉
    def clean(self, philor):
        self.forks[philor.leftFork.index].putdown()
        self.forks[philor.rightFork.index].putdown()
        self.forks_using[philor.leftFork.index] = False
        self.forks_using[philor.rightFork.index] = False


class Philosopher(threading.Thread):

    def __init__(self, index):
        threading.Thread.__init__(self)
        self.index = index
        self.leftFork = forks[self.index]
        self.rightFork = forks[(self.index + 1) % numForks]

    def run(self):
        while True:
            if waiter.serve(self):
                self.dining()
                waiter.clean(self)
            self.thinking()

    def dining(self):
        print ("Philosopher", self.index, " starts to eat.")
        sleep(random.uniform(1, 3) / 1000)
        print ("Philosopher", self.index, " finishes eating and leaves to think.")

    def thinking(self):
        sleep(random.uniform(1, 3) / 1000)


class Fork():

    def __init__(self, index):
        self.index = index
        self._lock = threading.Lock()

    def pickup(self):
        self._lock.acquire()

    def putdown(self):
        self._lock.release()

if __name__ == '__main__':
    # 创建服务生与哲学家实例
    waiter = Waiter()
    forks = [Fork(idx) for idx in range(numForks)]
    philosophers = [Philosopher(idx) for idx in range(numPhilosophers)]

    # 开启所有的哲学家线程
    for philosopher in philosophers:
        philosopher.start()

    # 方便 CTRL + C 退出程序
    try:
        while True:
            sleep(0.1)
    except Exception:
        pass
