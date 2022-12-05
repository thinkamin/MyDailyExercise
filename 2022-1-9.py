from my import gen_num

num_lst = gen_num()

def bubble_sort(A):
    length = len(A)
    for j in range(length):#0,n-1
        for i in range(1,length):#1,n-1
            if A[i-1]>A[i]:
                A[i-1],A[i]=A[i],A[i-1]
    return A
print('bubble_sort',bubble_sort(num_lst))



