from my import gen_num
from collections import namedtuple
#from my import G1,G2
#from collections import deque
num_lst = gen_num()
print(num_lst)

def merge_sort(A):
    length = len(A)
    if length==1:
        return A
    else:
        mid = length//2
        left = merge_sort(A[:mid])
        right = merge_sort(A[mid:])
        return merge(left,right)

def merge(left,right):
    len_left = len(left)
    len_right = len(right)
    i,j=0,0
    result = []
    while i<len_left and j<len_right:
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
        

def quick_sort(A):
    length = len(A)
    if length<=1:
        return A
    else:
        key = A.pop()
        lesser,greater=[],[]
        for elem in A:
            if elem < key:
                lesser.append(elem)
            else:
                greater.append(elem)
        return quick_sort(lesser)+[key]+quick_sort(greater)
print(quick_sort(num_lst))
