import  gen_num
num_lst = gen_num.gen_num1(10)
# print(num_lst)
def insert_sort(A):
    length = len(A)
    print(length)
    # print(A[7])
    for i in range(1,length):#[1,n-1]
        # print(i)
        key = A[i]
        j=i
        while A[j-1]>key and j>0:
            j-=1
        A[j+1:i+1]=A[j:i]
        A[j]=key
    return A
print(insert_sort(num_lst))
