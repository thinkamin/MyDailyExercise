import  gen_num
num_lst = gen_num.gen_num1(10)
print(num_lst)

def count_sort(A):
    max_value = max(A)
    min_value = min(A)
    count_lst = [0 for i in range(min_value,max_value+1)]
    for item in A:
        count_lst[item-min_value]+=1
    # print(count_lst)
    result = []
    for i in range(len(count_lst)):
        while count_lst[i]>0:
            print(min_value+i)
            result.append(min_value+i)
            count_lst[i]-=1
    return result
print(count_sort(num_lst))

