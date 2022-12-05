import  gen_num
num_lst = gen_num.gen_num1(10)
print(num_lst)
# from weighted_G import G
# from G import G 
def bubble_sort(A):
    length = len(A)
    for i in reversed(range(1,length)):
        for j in range(i):
            if A[j+1]<A[j]:
                A[j+1],A[j] = A[j],A[j+1]
    return A
print(bubble_sort(num_lst))

