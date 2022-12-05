import  gen_num
num_lst = gen_num.gen_num1(10)
print(num_lst)

def buildheap(A):
    length = len(A)
    mid = length//2
    for i in reversed(range(mid)):
        # print(i)
        heapify(A,i,length-1)
    return A

def heapify(A,idx,maxIdx):
    left = 2*idx+1
    right = 2*idx+2 
    largest = idx
    if left<=maxIdx and A[left]>A[idx]:
        largest = left
    if right<=maxIdx and A[right]>A[largest]:
        largest = right
    if  idx!=largest:
        A[largest],A[idx]=A[idx],A[largest]
        heapify(A,largest,maxIdx)
print(buildheap(num_lst))
