# -*- coding: utf-8 -*-
__author__ = 'QB'

from queue import Queue
import random, threading, time
'''
多对多的生产者消费者 Demo
'''

# 生产者类
class Producer(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self, name=name)
        self.data = queue

    def run(self):
        for i in range(5):
            print("%s 正在生产，向队列中生产 %d!" % (self.getName(), i))
            self.data.put(i)
            time.sleep(random.randrange(10) / 5)
        print("%s 完成生产!" % self.getName())


# 消费者类
class Consumer(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self, name=name)
        self.data = queue

    def run(self):
        for i in range(5):
            val = self.data.get()
            print("%s 正在消费，队列中的 %d 被消费!" % (self.getName(), val))
            time.sleep(random.randrange(10))
        print("%s 完成消费!" % self.getName())


def main():
    queue = Queue()
    producer = Producer('【生产者】', queue)
    consumer = Consumer('【消费者】', queue)
    # 开启生产者和消费者线程
    producer.start()
    consumer.start()
    # 等待子线程执行完成
    producer.join()
    consumer.join()
    print('所有线程执行完成!')


if __name__ == '__main__':
    main()
