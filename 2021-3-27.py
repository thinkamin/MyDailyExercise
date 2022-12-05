import gen_num
num_lst = gen_num.gen_num1(30)
print(num_lst)

def insert_sort(A):
    '''
    Args:
    A;num_lst
    '''
    length = len(A)
    for i in range(1,length):#[1,n-1]
        j = i
        key = A[j]
        while j>0 and key<A[j-1]:
            j = j-1
        A[j+1:i+1]=A[j:i]
        A[j]=key
    return A
print(insert_sort(num_lst))
