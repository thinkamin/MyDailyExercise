from my import gen_num
from collections import namedtuple
#from my import G1,G2
#from collections import deque
num_lst = gen_num()

def insertsort(A):
    length = len(A)
    for i in range(1,length):
        j=i
        key=A[j]
        while j-1>0 and A[j-1]>key:
            A[j]=A[j-1]
            j-=1
        A[j]=key
    return A

# print(insertsort(num_lst))
def shellsort(A):
    length = len(A)
    gaps = [8,4,2,1]
    for gap in gaps:
        if gap<length:
            for i in range(gap,length):
                j=i
                key=A[j]
                while j-gap>0 and A[j-gap]>key:
                    A[j]=A[j-gap]
                    j-=gap
                A[j]=key
    return A
print(shellsort(num_lst))

def mergesort(A):
    length = len(A)
    if length<=1:
        return A
    else:
        mid = length//2
        left = mergesort(A[:mid])
        right = mergesort(A[mid:])
        return merge(left,right)
def merge(left,right):
    len_l=len(left)
    len_r=len(right)
    i,j=0,0
    result=[]
    while i<len_l and j<len_r:
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result+= left[i:]
    result+= right[j:]
    return result
print(mergesort(num_lst))

def timsort(A):
    runs = []
    new_run = [A[0]]
    for i in range(1,len(A)):
        if A[i-1]<A[i]:
            new_run.append(A[i])
        else:
            runs.append(new_run)
            new_run=[]
            new_run.append(A[i])
    runs.append(new_run)

    result = []
    for run in runs:
        result = merge(result,run)
    return result
print(timsort(num_lst))


