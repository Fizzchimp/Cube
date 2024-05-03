from threading import Thread
import time

def myFunc(string):
    for i in range(10):
        print(string, i)
        time.sleep(0.5)
        
thread1 = Thread(target = myFunc, args = ("Thread 1:",))
thread2 = Thread(target = myFunc, args = ("Thread 2:",))

thread1.start()
time.sleep(0.1)
thread2.start()
time.sleep(0.1)
myFunc("Main:")