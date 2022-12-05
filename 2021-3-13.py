import gen_num

num_lst = gen_num.gen_num1(20)
# print(num_lst)
def select_sort(A):
    '''
    Args:
    A:num_lst
    '''
    length = len(num_lst)
    for i in reversed(range(1,length)):#[n-1,1]
        largest = A[0]
        for j in range(1,i+1):#[1,i]
            if A[j]>largest:
                largest = A[j]
        maxidx = A.index(largest)
        A[i],A[maxidx] = A[maxidx],A[i]
    return A
print(select_sort(num_lst))



