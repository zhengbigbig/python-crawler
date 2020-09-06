import threading

'''
多线程在同一个进程中进行的。因此在进程中的全局变量所有线程是共享的。
这样会造成，同时修改可能造成数据错误。需要使用锁来解决
在修改全局变量的地方，进行锁的操作。
'''
value = 0

gLock = threading.Lock()


def add_value():
	# 如果在函数中修改了全局变量，那么需要使用
	# global关键字进行申明
	global value
	gLock.acquire()
	for x in range(1000000):
		value += 1
	gLock.release()
	print("value的值是：%d" % value)


def main():
	for x in range(2):
		th = threading.Thread(target=add_value)
		th.start()


if __name__ == '__main__':
	main()
