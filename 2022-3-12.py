from my import gen_num
from collections import namedtuple

num_lst = gen_num()

def insert_sort(A):
    length = len(A)
    for i in range(1,length):#1,n-1
        j = i
        key = A[j]
        while j>0 and A[j-1]>key:
            A[j]=A[j-1]
            j-=1
        A[j]=key
    return A
# print(insert_sort(num_lst))
def shell_sort(A):
    gaps = [8,4,2,1]
    length = len(A)
    for gap in gaps:
        if length>gap:
            for i in range(gap,length):#gap,n-1
                j = i 
                key=A[j]
                while j-gap>=0 and A[j-gap]>key:
                    A[j]=A[j-gap]
                    j-=gap
                A[j]=key
    return A
# print(shell_sort(num_lst))
def merge_sort(A):
    length = len(A)
    if length<=1:
        return A
    else:
        mid = length//2
        left = merge_sort(A[:mid])
        right = merge_sort(A[mid:])
        return merge(left,right)

def merge(left,right):
    i,j=0,0
    result = []
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result+=left[i:]
    result+=right[j:]
    return result
# print(merge_sort(num_lst))

def quick_sort(A):
    length = len(A)
    if length<=1:
        return A
    else:
        key = A.pop()
        lesser,greater = [],[]
        for elem in A:
            if elem>key:
                greater.append(elem)
            else:
                lesser.append(elem)
        return quick_sort(lesser)+[key]+quick_sort(greater)
# print(quick_sort(num_lst))
def tim_sort(A):
    length = len(A)
    run = [A[0]]
    runs = []
    for i in range(1,length):
        if A[i]>A[i-1]:
            run.append(A[i])
        else:
            runs.append(run)
            run = []
            run.append(A[i])
    runs.append(run)
    print(runs)
    result = []
    for run in runs:
        result = merge(result,run)
    return result
print(tim_sort(num_lst))


