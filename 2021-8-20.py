import  gen_num
num_lst = gen_num.gen_num1(10)
print(num_lst)


def bubble_sort(A):
    length = len(A)
    for i in reversed(range(1,length)):
        for j in range(1,i+1):
            if A[j]<A[j-1]:
                A[j],A[j-1]=A[j-1],A[j]
    return A
print(bubble_sort(num_lst))

def select_sort(A):
    length = len(A)
    for i in reversed(range(1,length)):
        max_value = A[0]
        for j in range(i+1):
            max_value=max(max_value,A[j])
        max_idx = A.index(max_value)
        A[i],A[max_idx] = A[max_idx],A[i]
    return A
print(select_sort(num_lst))
