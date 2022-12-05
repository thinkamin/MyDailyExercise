import functools
import time

@functools.lru_cache()
def fab(n):
    if n<=1:
        return n
    else:
        return fab(n-2)+fab(n-1)



def fab2(n):
    if n<=1:
        return n 
    else:
        return fab2(n-2)+fab2(n-1)

t0 = time.time()
print(fab(40))
t1 = time.time()
print('fab',t1-t0)

t2=time.time()
print(fab2(40))
t3=time.time()
print('fab2',t3-t2)
