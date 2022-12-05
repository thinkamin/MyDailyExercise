#heap sort
import random
num_list = list(range(10))#[0,9]
random.shuffle(num_list)

def buildHeap(A):
    '''
    Args:
    A:num_list
    '''
    length = len(A)
    for i in  [length//2-x-1 for x in range(1,length//2)]:
        heapify(A,i,length-1)

def heapify(A,idx,maxIdx):
    left = 2*idx + 1
    right =2*idx + 2
    if left<maxIdx and A[left]>A[idx]:
        largest = left
    else:
        largest = idx
    if right<maxIdx and A[right]>A[largest]:
        largest = right
    if largest != idx:
        A[idx],A[largest]=A[largest],A[idx]
        heapify(A,largest,maxIdx)

print('origin list:',num_list)
buildHeap(num_list)
print(num_list)
length = len(num_list)
for i in [length-x for x in range(1,length)]:
    num_list[0],num_list[i] = num_list[i],num_list[0]
    heapify(num_list,0,i)
print(num_list)
