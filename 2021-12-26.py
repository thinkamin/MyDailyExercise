from myutils import gen_num
import heapq


num_lst = gen_num()
print(num_lst)
def bubble_sort(A):
    length = len(A)
    for j in reversed(range(1,length+1)):#n,1
        for i in range(1,j):#1,j-1
            if A[i-1]>A[i]:
                A[i-1],A[i]=A[i],A[i-1]
    return A
print(bubble_sort(num_lst))

def max_sort(A):
    length = len(A)
    for j in reversed(range(1,length+1)):
        largest = A[0]
        for i in range(j):
            if A[i]>largest:
                largest=A[i]
        # print(i)
        max_index = A.index(largest)
        A[max_index],A[i]=A[i],A[max_index]
    return A
print(max_sort(num_lst))

def heap_sort(A):
    length = len(A)
    heapq.heapify(A)
    result = [ heapq.heappop(A)  for i in range(length)]
    return result
print(heap_sort(num_lst))
