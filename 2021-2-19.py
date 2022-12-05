'''
insert sort upgrade
'''
import gen_num
num_lst = gen_num.gen_num1(100)
# print(num_lst)
def insert_sort(A):
    '''
    Args:
        A:num_lst
    '''
    length = len(A)
    for i in range(1,length):#[1,length-1]
        key = A[i]
        while i>0 and A[i-1]>key:
            A[i]=A[i-1]
            i -=1
        A[i] = key
    return A
print(insert_sort(num_lst))


    


