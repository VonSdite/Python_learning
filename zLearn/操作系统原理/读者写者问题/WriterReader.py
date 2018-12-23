# -*- coding: utf-8 -*-
# __Author__: Sdite
# __Email__ : a122691411@gmail.com

from threading import *
import time
import random

condition = Condition()
lock = Lock()
ReaderCount = 0


class Writer(Thread):
    """docstring for Writer"""

    def __init__(self):
        super(Writer, self).__init__()

    def run(self):
        while True:
            condition.acquire()
            print("Writer write somthing...")
            condition.notify()
            condition.release()
            time.sleep(random.random())


class Reader(Thread):
    """docstring for Reader"""

    def __init__(self):
        super(Reader, self).__init__()

    def run(self):
        global ReaderCount
        while True:
            lock.acquire()
            if ReaderCount == 0:
                condition.acquire()
                print("Wait the writer")
                condition.wait()
                print("Start to read...")
            ReaderCount += 1
            print("%d reader(s) start to read..." % ReaderCount)
            lock.release()
            time.sleep(random.random())

            lock.acquire()
            ReaderCount -= 1
            print("One reader quit to read...")
            if ReaderCount == 0:
                condition.release()
            lock.release()
            time.sleep(random.random())

if __name__ == '__main__':
    Reader().start()
    Writer().start()

