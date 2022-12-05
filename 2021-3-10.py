import gen_num
num_lst = gen_num.gen_num1(20)
print('origin:',num_lst)

def select_sort(A):
    '''
    Args:
    A;num_lst
    '''
    length = len(A)
    for  i in reversed(range(1,length)):#[n-1,1]
        largest = A[0]
        for j in range(i+1):#[0,i]
            if A[j]>largest:
                largest = A[j]
        max_idx = A.index(largest)
        A[i],A[max_idx]=A[max_idx],A[i]
        print(A)
    return A
print(select_sort(num_lst))

            


        


