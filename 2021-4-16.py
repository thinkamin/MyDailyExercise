import gen_num
num_lst = gen_num.gen_num2(20)
print(num_lst)

def count_sort(A):
    '''
    Args:
    A:num_lst
    '''
    min_value = min(A)
    max_value = max(A)
    count = [0 for i in range(min_value,max_value+1)]#[min_value,max_value]
    for i in A:
        count[i-min_value] +=1
    result = []
    for j in range(len(count)):#[0,n-1]
        while count[j]>0:
            result.append(min_value+j)
            count[j] -=1
    return result

print(count_sort(num_lst))



