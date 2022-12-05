import gen_num
num_lst = gen_num.gen_num1(20)
print(num_lst)

def insertsort(A):
    '''
    Args:
    A;num_lst
    '''
    length = len(A)
    for i in range(1,length):#[1,n-1]
        j = i
        key = A[i]
        while i>0 and key <A[i-1]:
            i -=1
        A[i+1:j+1]=A[i:j]
        A[i]=key
    return A
print(insertsort(num_lst))

