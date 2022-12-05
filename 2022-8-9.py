from my import gen_num
from collections import namedtuple
#from my import G1,G2
#from collections import deque
num_lst = gen_num()
print(num_lst)
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
    left_length = len(left)
    right_length = len(right)
    i,j=0,0
    result = []
    while i<left_length and j<right_length:
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result+=left[i:]
    result+=right[j:]
    return result

print(merge_sort(num_lst))

def tim_sort(A):
    length = len(A)
    runs,sorted_runs=[],[]
    new_run = [A[0]]
    sorted_array = []
    i =1 
    while i <length:
        if A[i]<A[i-1]:
            runs.append(new_run)
            new_run=[A[i]]
        else:
            new_run.append(A[i])
        i+=1
    runs.append(new_run)

    for run in runs:
        sorted_array = merge(sorted_array,run)
    return sorted_array

print(tim_sort(num_lst))



def quick_sort(A):
    length=len(A)
    if length<=1:
        return A
    else:
        key = A.pop()
        lesser,greater=[],[]
        for elem in A:
            if elem<key:
                lesser.append(elem)
            else:
                greater.append(elem)
        return quick_sort(lesser)+[key]+quick_sort(greater)

print(quick_sort(num_lst))
