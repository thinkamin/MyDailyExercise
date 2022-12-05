import  gen_num

num_lst1 = gen_num.gen_num1(10)
num_lst2 = list(reversed(gen_num.gen_num1(10)))
print(num_lst1)
print(num_lst2)

num_lst = list(zip(num_lst1,num_lst2))
print(num_lst)
result = sorted(num_lst,key=lambda x:x[1])
print(result)


