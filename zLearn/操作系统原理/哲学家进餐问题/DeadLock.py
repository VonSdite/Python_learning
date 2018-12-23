#-*- coding:utf-8 -*-

import threading
from time import sleep
import os
import random

# 设置为2更容易重现死锁
numPhilosophers = numForks = 2


class Philosopher(threading.Thread):

    def __init__(self, index):
        threading.Thread.__init__(self)
        self.index = index
        self.leftFork = forks[self.index]
        self.rightFork = forks[(self.index + 1) % numForks]

    def run(self):
        while True:
            self.leftFork.pickup()
            self.rightFork.pickup()
            self.dining()
            self.leftFork.putdown()
            self.rightFork.putdown()
            self.thinking()

    def dining(self):
        print("Philosopher", self.index, " starts to eat.")
        sleep(random.uniform(1, 3) / 1000)
        print("Philosopher", self.index, " finishes eating and leaves to think.")

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
    # 创建叉子与哲学家实例
    forks = [Fork(idx) for idx in range(numForks)]
    philosophers = [Philosopher(idx) for idx in range(numPhilosophers)]

    # 开启所有的哲学家线程
    for philosopher in philosophers:
        philosopher.start()

    # 方便 CTRL + C 退出程序
    try:
        while True:
            sleep(0.1)
    except Exception as e:
        raise e
