import  gen_num
import heapq

num_lst = gen_num.gen_num1(10)
# print(num_lst)
heapq.heapify(num_lst)
print(num_lst)

length = len(num_lst)
result = [heapq.heappop(num_lst) for i in range(length)]
print(result)
