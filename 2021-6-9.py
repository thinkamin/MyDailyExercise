import  gen_num
num_lst = gen_num.gen_num1(10)
print(num_lst)

def insert_sort(A):
    length = len(A)
    for i in range(1,length):#[1,n-1]
        key = A[i]
        j = i 
        while A[j-1]>key and j>0:
            j -= 1
            print(i,j)
        A[j+1:i+1]=A[j:i]
        A[j]=key
        print(i,A)
    return A    
print(insert_sort(num_lst))

