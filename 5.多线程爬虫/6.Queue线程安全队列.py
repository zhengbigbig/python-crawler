from queue import Queue
import random
import time
import threading

'''

在线程中，访问一些全局变量，加锁是一个经常的过程。如果你是想把一些数据存储到某个队列中，那么Python内置了一个线程安全的模块叫做queue模块。Python中的queue模块中提供了同步的、线程安全的队列类，包括FIFO（先进先出）队列Queue，LIFO（后入先出）队列LifoQueue。这些队列都实现了锁原语（可以理解为原子操作，即要么不做，要么都做完），能够在多线程中直接使用。可以使用队列来实现线程间的同步。相关的函数如下：
初始化Queue(maxsize)：创建一个先进先出的队列。
1. qsize()：返回队列的大小。
2. empty()：判断队列是否为空。
3. full()：判断队列是否满了。
4. get()：从队列中取最后一个数据。默认情况下是阻塞的，也就是说如果队列已经空了，那么再调用就会一直阻塞，直到有新的数据添加进来。也可以使用`block=False`，来关掉阻塞。如果关掉了阻塞，在队列为空的情况获取就会抛出异常。
5. put()：将一个数据放到队列中。跟get一样，在队列满了的时候也会一直阻塞，并且也可以通过block=False来关掉阻塞，同样也会抛出异常。
'''


# q = Queue(4)
#
# for x in range(5):
#     try:
#         q.put(x, block=False)
#     except:
#         break
#
# if q.full():
#     print("满了")

# print(q.qsize())


# for x in range(5):
#     try:
#         value = q.get(block=False)
#     except:
#         break
#     print(value)
#
# if q.empty():
#     print("空了")
#
# print("完成")


def add_value(q):
	while True:
		q.put(random.randint(0, 10))
		time.sleep(1)


def get_value(q):
	while True:
		print("获取到的值：%d" % q.get())


def main():
	q = Queue(10)
	th1 = threading.Thread(target=add_value, args=[q])
	th2 = threading.Thread(target=get_value, args=[q])

	th1.start()
	th2.start()


if __name__ == '__main__':
	main()
