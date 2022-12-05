import  gen_num
num_lst = gen_num.gen_num1(10)
print(num_lst)
def select_sort(A):
    length = len(A)
    for i in reversed(range(1,length)):#[n-1,1]
        max_value = A[0]
        for j in range(i+1):
            if A[j]>max_value:
                max_value = A[j]
        max_value_index = A.index(max_value)
        A[j],A[max_value_index]=A[max_value_index],A[j]
    return A
print(select_sort(num_lst))



