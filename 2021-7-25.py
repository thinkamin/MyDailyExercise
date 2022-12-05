import  gen_num
num_lst = gen_num.gen_num1(10)
print(num_lst)


def bulid_heap(A):
    length = len(A)
    for i in reversed(range(length//2)):#[0,n//2-1]
        heapify(A,i,length-1)

def heapify(A,idx,maxId):
    '''
    大顶堆
    '''
    left = 2*idx+1
    right = 2*idx+2
    if left<maxId and A[left]>A[idx]:
        largest = left
    else:
        largest = idx
    if right<maxId and A[right]>A[largest]:
        largest = right
    if idx!= largest:
        A[idx],A[largest] = A[largest],A[idx]
        heapify(A,largest,maxId)

bulid_heap(num_lst)
length = len(num_lst)
print(num_lst)
for i in reversed(range(1,length)):
    num_lst[0],num_lst[i]=num_lst[i],num_lst[0]
    heapify(num_lst,0,i)
print(num_lst)
