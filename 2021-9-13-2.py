#import  gen_num
num_lst = gen_num.gen_num1(10)
print(num_lst)

def quick(A):
    maxIdx = len(A)-1
    i=0
    j=len(A)-2
    while i<j:
        key = A[maxIdx]
        if A[i]>key:
            if A[j]<key:
                A[i],A[j]=A[j],A[i]
            else:
                j-=1
        else:
            i+=1

