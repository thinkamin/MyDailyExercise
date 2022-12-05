from my import gen_num
from collections import namedtuple
#from my import G1,G2
#from collections import deque
num_lst = gen_num()
print(num_lst)

def insert_sort(A):
    length= len(A)
    for i in range(1,length):#1,n-1
        j = i
        key = A[j]
        while j>0 and A[j-1]>key:
            A[j]=A[j-1]
            j-=1
        A[j]=key
    return A
# print(insert_sort(num_lst))

def shell_sort(A):
    gaps = [8,4,2,1]
    length = len(A)
    count = 0
    for gap in gaps:
        if gap<length:
            for i in range(gap,length):#gap,n-1
                j = i
                key = A[j]
                while j>0 and A[j-gap]>key:
                    A[j]=A[j-gap]
                    j-=gap
                    count+=1
                A[j]=key
            print(gap,A)
    print(count)
    return A
print(shell_sort(num_lst))

