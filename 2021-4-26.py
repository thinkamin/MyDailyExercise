import gen_num 
num_lst = gen_num.gen_num2(15)
print(num_lst)
def count_sort(A):
    '''
    Args:
    A:num_lst
    '''
    max_value = max(A)
    min_value = min(A)
    count_list =[0 for i in range(min_value,max_value+1)]
    for num in A:
        count_list[num-min_value] +=1

    result = []
    for i in range(len(count_list)):#[0,n-1]
        if count_list[i]>0:
            result.append(i+min_value)
    return result 
print(count_sort(num_lst))


