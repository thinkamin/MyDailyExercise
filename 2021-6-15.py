import  gen_num
num_lst = gen_num.gen_num1(10)
print(num_lst)

def select_sort(A):
    length = len(A)
    for i in reversed(range(length)):#[n-1,0]
        max_value = A[0]
        for j in range(i+1):#[0,i-1]
            if A[j]>max_value:
                max_value = A[j]
        max_index = A.index(max_value)
        A[i],A[max_index]=A[max_index],A[i]
    return A

print(select_sort(num_lst))




