
'''
exercise heapq
'''
import heapq 
import gen_num

num_lst = gen_num.gen_num1(20)
# print(num_lst)
heapq.heapify(num_lst)
result = [heapq.heappop(num_lst) for _ in range(len(num_lst))]
print(result)
