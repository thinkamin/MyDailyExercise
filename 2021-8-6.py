import  gen_num
num_lst = gen_num.gen_num2(20)
print(num_lst)
max_value = (max(num_lst))
length = len(str(max_value))

for i in range(length):
    buckets = [[] for _ in range(10)]

    for elem in num_lst:
        tmp = int((elem/(10**i))%10)
        buckets[tmp].append(elem)
    print(i,buckets)
    a=0
    for buck in buckets:
        for i in buck:
            num_lst[a] = i
            a+=1
print(num_lst)


