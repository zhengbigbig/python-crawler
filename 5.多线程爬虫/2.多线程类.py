import time
import threading

'''
1. threading.current_thread：在线程中执行这个函数，会返回当前线程的对象。
2. threading.enumerate：获取整个程序中所有的线程。
'''

class CodingThread(threading.Thread):
	def run(self):
		the_thread = threading.current_thread()
		for x in range(3):
			print("%s正在写代码..." % the_thread.name)
			time.sleep(1)


class DrawingThread(threading.Thread):
	def run(self):
		the_thread = threading.current_thread()
		for x in range(3):
			print("%s正在画图..." % the_thread.name)
			time.sleep(1)


def multi_thread():
	th1 = CodingThread()
	th2 = DrawingThread()
	th1.start()
	th2.start()


if __name__ == '__main__':
	multi_thread()
