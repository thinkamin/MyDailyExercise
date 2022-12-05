import  gen_num
num_lst = gen_num.gen_num1(10)
print(num_lst)

def heapify(A,index):
    maxIndex = len(A)-1
    largest = index
    left_index = 2*index +1
    right_index = 2*index +2
    if left_index<maxIndex and A[left_index]>A[largest]:
        largest = left_index
    if right_index<maxIndex and A[right_index]>A[largest]:
        largest = right_index
    if largest != index:
        A[largest],A[index]=A[index],A[largest]
        heapify(A,largest)

def heap_sort(A):
    n = len(A)
    for i in reversed(range(n//2-1)):
        heapify(A,i)

    for i in reversed(range(1,n)):
        A[0],
    


