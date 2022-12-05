import gen_num
import heapq

num_lst = gen_num.gen_num1(30)
# print(num_lst)
heapq.heapify(num_lst)
# print(num_lst)
result = [heapq.heappop(num_lst) for _ in range(len(num_lst))]
print(result)
