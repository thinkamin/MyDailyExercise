import gen_num  
num_lst  =gen_num.gen_num1(10)
# print(num_lst)

def count_sort(A):
    '''
    Args:
    A:num_lst
    '''
    min_num = min(A)
    max_num = max(A)
    count_lst = [0 for i in range(len(A))]
    for num in A:
        count_lst[num-min_num]+=1
    # print(count_lst)
    result = []
    for j in range(len(count_lst)):
        while count_lst[j]>0:
            result.append(j+min_num)
            count_lst[j] -=1
    return result
print(count_sort(num_lst))

