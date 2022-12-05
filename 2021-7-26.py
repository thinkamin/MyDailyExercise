import  gen_num
num_lst = gen_num.gen_num1(10)
print(num_lst)

def select_sort(A):
    length = len(A)
    for i in reversed(range(1,length)):#[0,n-1]
        max_value = A[0]
        for j in range(i+1):#[0,i]
            max_value = max(A[j],max_value)
        max_index = A.index(max_value)
        A[max_index],A[j]=A[j],A[max_index]
    return A
print(select_sort(num_lst))



