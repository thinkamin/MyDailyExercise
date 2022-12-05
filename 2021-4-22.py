import gen_num  
num_lst = gen_num.gen_num1(10)
# print(num_lst)
def bubble_sort(A):
    '''
    Args:
    A:num_lst
    '''
    length = len(A)
    for i in reversed(range(1,length)):#[1,n-1]
        for j in range(i):#[0,i]
            if A[j]>A[j+1]:
                A[j],A[j+1]=A[j+1],A[j]
    return A
print(bubble_sort(num_lst))
