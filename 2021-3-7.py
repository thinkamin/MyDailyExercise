import gen_num
num_lst = gen_num.gen_num2(20)
print(num_lst)
print(sorted(num_lst))
min_num = min(num_lst)
max_num = max(num_lst)

count = [0 for _ in range(max_num-min_num+1)]#[0,max-min]
# print(count)
for i in num_lst:
    count[i-min_num] = count[i-min_num]+1
print(count)

result = []
for j in range(len(count)):
    while count[j]>0:
        result.append(j+min_num)
        count[j] = count[j]-1
print(result)

