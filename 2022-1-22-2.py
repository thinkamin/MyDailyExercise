import threading
import time

def test():
    print('job1')
    time.sleep(1)
    print('job finish')

a = threading.Thread(target=test) 
# a.setDaemon(True)
a.start()
# a.join()
print('finish')
