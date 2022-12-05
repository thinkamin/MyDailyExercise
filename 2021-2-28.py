'''
random choice for insert sort
'''
import gen_num
num_lst = gen_num.gen_num1(20)
# print(num_lst)

def insertsort(A):

    '''
    Args:
        A;num_lst
    '''
    length = len(A)
    for i in range(1,length):#[1,n-1]
        while i>0 and A[i]<A[i-1]:
            A[i],A[i-1]=A[i-1],A[i]
            i -=1
    return A
print(insertsort(num_lst))
