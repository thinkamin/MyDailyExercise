import  gen_num
num_lst = gen_num.gen_num1(10)
print(num_lst)

def select_sort(A):
    length = len(A)
    for i in reversed(range(1,length)):
        max_value = A[0]
        for j in range(i+1):
            max_value = max(max_value,A[j])
        idx = A.index(max_value)
        A[j],A[idx]=A[idx],A[j]
    return A
print(select_sort(num_lst))

