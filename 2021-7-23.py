import  gen_num
num_lst = gen_num.gen_num2(20)
print(num_lst)

def count_sort(A):
    min_value = min(A)
    max_value = max(A)
    count_lst = [0 for i in range(min_value,max_value+1)]

    for item in A:
        count_lst[item-min_value]+=1

    result = []
    for i in range(len(count_lst)):#[0,n-1]
        while count_lst[i]>0:
            result.append(i+min_value)
            count_lst[i]-=1
    return result
print(count_sort(num_lst))



