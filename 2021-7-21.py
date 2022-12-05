import  gen_num

num_lst = gen_num.gen_num1(10)
print(num_lst)

def select_sort(A):
    length = len(A)
    for i in reversed(range(1,length)):#[1,n-1]
        max_value = A[0]
        for j in range(1,i+1):#[1,i]
            if A[j]>max_value:
                max_value = A[j]
        idx = A.index(max_value)
        A[idx],A[i] = A[i],A[idx]
    return A
print(select_sort(num_lst))
