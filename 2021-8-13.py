#import  gen_num
num_lst = gen_num.gen_num1(10)
print(num_lst)


def build_heap(A):
    length = len(A)
    maxidx = length-1
    for i in reversed(range(length//2-1)):
        heapify(A,i,maxidx)





def heapify(A,idx,maxidx):
    left_child = 2*idx+1
    right_child = 2*idx+2
    if left_child<maxidx:
        if A[idx]>A[left_child]:
            largest = idx
        else:
            largest = left_child
    if right_child<maxidx:
        if A[largest]<A[right_child]:
            largest = right_child

    if idx!=largest:
        A[idx],A[largest] = A[largest],A[idx]
        heapify(A,largest,maxidx)



