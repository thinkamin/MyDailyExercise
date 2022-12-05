import  gen_num
num_lst = gen_num.gen_num1(10)
# print(num_lst)
def insert_sort(A):
    '''
    A:num_lst
    '''
    length = len(A)
    for i in range(1,length):#[1,n-1]
        j=i
        key = A[i]
        while A[j-1]>key and j>0:
            A[j]=A[j-1]
            j-=1
        A[j]=key
    return A
print(insert_sort(num_lst))
