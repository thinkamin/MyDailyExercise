import gen_num
import heapq
num_lst = gen_num.gen_num1(100)
print(num_lst)
print(heapq.heapify(num_lst))
print(num_lst)
def heap_sort(A):

    '''
    Args:
    A:num_lst
    '''
    heapq.heapify(A)
    result = [heapq.heappop(A) for i in range(len(A))]
    return result
print(heap_sort(num_lst))
