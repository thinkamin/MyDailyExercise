from my import gen_num
from collections import namedtuple
#from my import G1,G2
#from collections import deque
# num_lst = gen_num()

def fab(n):
    if n<=1:
        return 1
    else:
        return n*fab(n-1)
for i in range(10):
    print("{},{}".format(i,fab(i)))


def fab2(n):
    if n<3:
        return 1
    else:
        return fab2(n-1)+fab2(n-2)
for i in range(1,10):
    print("{},{}".format(i,fab2(i)))
