import heapq
import gen_num

num_lst = gen_num.gen_num1(10)
# print(num_lst)
heapq.heapify(num_lst) #默认最小堆
# print(num_lst)
heapq.heapify(num_lst[1:])#切片无效
# print(num_lst)
print('*'*10)
def heapsort(A):

    '''
    Args:
    A:num_lst
    '''
    heap=[]
    for item in A:
        heapq.heappush(heap,item)
    result = [heapq.heappop(heap) for _ in range(len(A))]   
    return result
result= heapsort(num_lst)
# print(result)
def heapsort2(A):
    heapq.heapify(A)
    result = [heapq.heappop(A) for _ in  range(len(A))]
    return result
print(heapsort2(num_lst))
       
