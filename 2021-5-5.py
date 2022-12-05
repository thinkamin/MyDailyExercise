import gen_num
num_lst = gen_num.gen_num1(10)
# print(num_lst)
def bubble_sort(A):
    length = len(A)
    for i in reversed(range(1,length)):#[n-1,1]
        for j in range(i):#[0,i]
            if A[j]>A[j+1]:
                A[j],A[j+1]=A[j+1],A[j]
    return A
print(bubble_sort(num_lst))

