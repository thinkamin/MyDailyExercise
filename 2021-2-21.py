'''
bubble_sort
'''
import gen_num
num_lst = gen_num.gen_num1(20)
# print(num_lst)
def bubble_sort(A):
    '''
    Args:
        A:num_lst
    '''
    length = len(A)
    for i in [length-x for x in range(length)]:#[n,1]
        for j in range(len(A[:i-1])):
            if A[j]>A[j+1]:
                A[j],A[j+1] = A[j+1],A[j]
        print(A) 
    return A

print(bubble_sort(num_lst))
