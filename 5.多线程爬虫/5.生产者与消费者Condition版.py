'''
Lock版本的生产者与消费者模式可以正常的运行。
但是存在一个不足，在消费者中，总是通过while True死循环并且上锁的方式去判断钱够不够。
上锁是一个很耗费CPU资源的行为。因此这种方式不是最好的。
还有一种更好的方式便是使用threading.Condition来实现。
threading.Condition可以在没有数据的时候处于阻塞等待状态。
一旦有合适的数据了，还可以使用notify相关的函数来通知其他处于等待状态的线程。
这样就可以不用做一些无用的上锁和解锁的操作。可以提高程序的性能。
首先对threading.Condition相关的函数做个介绍，threading.Condition类似threading.Lock，
可以在修改全局数据的时候进行上锁，也可以在修改完毕后进行解锁。以下将一些常用的函数做个简单的介绍：
1. acquire：上锁。
2. release：解锁。
3. wait：将当前线程处于等待状态，并且会释放锁。可以被其他线程使用notify和notify_all函数唤醒。被唤醒后会继续等待上锁，上锁后继续执行下面的代码。
4. notify：通知某个正在等待的线程，默认是第1个等待的线程。
5. notify_all：通知所有正在等待的线程。notify和notify_all不会释放锁。并且需要在release之前调用。


'''

import threading
import random
import time

gMoney = 0
gCondition = threading.Condition()
gTimes = 0


class Producer(threading.Thread):
	def run(self) -> None:
		global gMoney
		global gTimes
		while True:
			gCondition.acquire()
			if gTimes >= 10:
				gCondition.release()
				break
			money = random.randint(0, 100)
			gMoney += money
			gTimes += 1
			print("%s生产了%d元钱，剩余%d元钱" % (threading.current_thread().name, money, gMoney))
			gCondition.notify_all()
			gCondition.release()
			time.sleep(1)


class Consumer(threading.Thread):
	def run(self) -> None:
		global gMoney
		while True:
			gCondition.acquire()
			money = random.randint(0, 100)
			while gMoney < money:
				if gTimes >= 10:
					print("%s想消费%d元钱，但是余额只有%d元钱了，并且生产者已经不再生产了！" % (threading.current_thread().name, money, gMoney))
					gCondition.release()
					return  # 函数直接返回，break只能退出一层循环
				print("%s想消费%d元钱，但是余额只有%d元钱了，消费失败！" % (threading.current_thread().name, money, gMoney))
				gCondition.wait()
			gMoney -= money
			print("%s消费了%d元钱，剩余%d元钱" % (threading.current_thread().name, money, gMoney))
			gCondition.release()
			time.sleep(1)


def main():
	for x in range(5):
		th = Producer(name="生产者%d号" % x)
		th.start()

	for x in range(5):
		th = Consumer(name="消费者%d号" % x)
		th.start()


if __name__ == '__main__':
	main()
