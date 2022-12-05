from my import gen_num
from collections import namedtuple
#from my import G1,G2
#from collections import deque
num_lst = gen_num()

def buildheap(A):
    length = len(A)
    for i in reversed(range(length//2)):
        heapify(A,i,length)

def heapify(A,idx,maxIdx):
    left = 2*idx+1
    right = 2*idx+2
    
    if right < maxIdx and A[right] < A[idx]:
        largest = right
    else:
        largest = idx
    if left < maxIdx and A[left] < A[largest]:
        largest = left

    if largest != idx:
        A[idx],A[largest]=A[largest],A[idx]
        heapify(A,largest,maxIdx)


buildheap(num_lst)
result = []
for i in range(len(num_lst)):
    key = num_lst.pop(0)
    result.append(key)
    buildheap(num_lst)
print(result)

