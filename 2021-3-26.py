import gen_num
num_lst = gen_num.gen_num1(30)
# print(num_lst)
def select_sort(A):
    '''
    Args:
    A:num_lst
    '''
    length = len(A)
    for i in reversed(range(1,length)):#[n-1,1]
        largest = A[0]
        for j in range(i):
            if A[j]>largest:
                largest = A[j]
        max_index = A.index(largest)
        A[max_index],A[i] = A[i],A[max_index]
    return A
print(select_sort(num_lst))

