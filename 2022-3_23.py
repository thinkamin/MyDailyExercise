import threading
def func1(message):
    for i in range(100):
        print(message)


t = threading.Thread(target=func1,args="G").start()
t1 = threading.Thread(target=func1,args="N").start()
