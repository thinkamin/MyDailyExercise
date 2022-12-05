'''
heap sort
像select sort 和bubblesort 一样 每次从剩余lst中找最大的
heap sort可以看作是他们两个的升级版
'''
import gen_num
num_lst = gen_num.gen_num1(20)
# print(num_lst)


def heapify(A,idx,maxIdx):
    '''
    建堆：使得每个子堆的最大值都在三角的顶部
    '''
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

def build_heap(A):
    '''
    Args:
    A:num_lst
    '''
    length = len(A)
    for i in [length//2-x-1 for x in range(1,length//2)]:
        heapify(A,i,length-1)

def heap_sort(A):
    build_heap(A)
    length = len(A) 
    for i in [length-x for x in range(1,length)]: #
        A[0],A[i] = A[i],A[0]
        heapify(A,0,i)
        print(A)
    return A
print(heap_sort(num_lst))
