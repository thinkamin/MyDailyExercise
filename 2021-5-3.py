import gen_num 
num_lst  = gen_num.gen_num1(10)
print(num_lst)
def insert_sort(A):
    '''
    Args:
    A:num_lst
    '''
    length = len(A)
    for i in range(1,length):#[0,n-1]
        j = i 
        key = A[i]
        while A[j-1]>key and j>0:
            j-=1
        A[j+1:i+1]=A[j:i]
        A[j]=key
    return A
print(insert_sort(num_lst))
