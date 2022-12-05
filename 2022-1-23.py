import threading
import time

def test1():
    print('job1')
    time.sleep(1)
    print('job1 finish')
def test2():
    print('job2')
    time.sleep(2)
    print('job2 finish')

a = threading.Thread(target=test1) 
b = threading.Thread(target=test2) 
a.setDaemon(True)
a.start()
# a.join()
b.setDaemon(True)
b.start()
# b.join()
print('finish')
