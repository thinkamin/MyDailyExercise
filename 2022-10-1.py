from my import gen_num
from collections import namedtuple
#from my import G1,G2
#from collections import deque
num_lst = gen_num()

def insert_sort(A):
    length = len(A)
    for i in range(1,length):
        j=i
        key = A[j]
        while j-1>=0 and A[j-1]>key:
            A[j]=A[j-1]
            j-=1
        A[j]=key
    return A
print(insert_sort(num_lst))
