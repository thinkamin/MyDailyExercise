import  gen_num
num_lst = gen_num.gen_num1(10)
print(num_lst)

def insert_sort(A):
    length = len(A)
    for i in range(1,length):
        j = i 
        key = A[j]
        while A[j-1]>key and j>0:
            A[j]=A[j-1]
            j-=1
        A[j]=key
    return A
# print(insert_sort(num_lst))

def shell_sort(A):
    length = len(A)
    gaps = [8,4,2,1]
    for gap in gaps:
        if gap<length:
            for i in range(gap,length):
                j = i
                key = A[j]
                while A[j-gap]>key and j-gap>=0:
                    A[j]=A[j-gap]
                    j = j-gap
                A[j]=key
    return A
print(shell_sort(num_lst))



        
