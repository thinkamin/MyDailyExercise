import  gen_num
num_lst = gen_num.gen_num1(10)
print(num_lst)

def build_heap(A):
    length = len(A)
    for i in reversed(range(length//2)):
        print(i)
        heapify(A,i,length-1)

def heapify(A,idx,maxIdx):
    left = 2*idx+1
    right = 2*idx+2
    if left<maxIdx and A[left]>A[idx]:
        largest = left
    else:
        largest = idx
    if right<maxIdx and A[right]>A[largest]:
        largest = right
    if largest != idx:
        A[idx],A[largest] = A[largest],A[idx]
        heapify(A,largest,maxIdx)

build_heap(num_lst)
print(num_lst)
for i  in reversed(range(1,len(num_lst))):
    num_lst[0],num_lst[i] = num_lst[i],num_lst[0]
    heapify(num_lst,0,i)
print(num_lst)
