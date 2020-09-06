import threading
import random
import time

gMoney = 0
gLock = threading.Lock()
gTimes = 0


class Producer(threading.Thread):
	def run(self) -> None:  # 提示作用  返回值
		global gMoney
		global gTimes
		while True:
			gLock.acquire()
			if gTimes >= 10:
				gLock.release()
				break
			money = random.randint(0, 100)
			gMoney += money
			gTimes += 1
			print("%s生产了%d元钱" % (threading.current_thread().name, money))
			gLock.release()
			time.sleep(1)


class Consumer(threading.Thread):
	def run(self) -> None:
		global gMoney
		while True:
			gLock.acquire()
			money = random.randint(0, 100)
			if gMoney >= money:
				gMoney -= money
				print("%s消费了%d元钱" % (threading.current_thread().name, money))
			else:
				if gTimes >= 10:
					gLock.release()
					break
				print("%s想消费%d元钱，但是余额只有%d" % (threading.current_thread().name, money, gMoney))
			gLock.release()
			time.sleep(1)


def main():
	for x in range(5):
		th = Producer(name="生产者%d号" % x)
		th.start()

	for x in range(5):
		th = Consumer(name="消费者%d号" % x)
		th.start()
	time.sleep(5)
	print(gMoney)

if __name__ == '__main__':
	main()

