import gen_num
num_lst = gen_num.gen_num1(20)
# print(num_lst)
def bubblesort(A):
    '''
    Args:
    A:num_lst
    '''
    length = len(A)
    for i in reversed(list(range(length))):#[n-1,0]
        for j in range(i):#[0,i-1]
            if A[j]>A[j+1]:
                A[j],A[j+1] = A[j+1],A[j]
    return A
print(bubblesort(num_lst))


