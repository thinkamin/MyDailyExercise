import  gen_num
import heapq 

num_lst = gen_num.gen_num1(10)
heapq.heapify(num_lst)
result = [heapq.heappop(num_lst) for i in range(len(num_lst))]
print(result)

