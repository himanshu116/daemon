from threading import*
import time
def m1():
	for i in range(5):
		print("thread nature",current.thread().isDaemon())
		time.slepp(3)
t=Thread(target=m1)
t.setDaemon(True)
t.start()
print("inside main non daemon thread")