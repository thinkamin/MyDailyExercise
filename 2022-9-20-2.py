from my import gen_num
from collections import namedtuple
#from my import G1,G2
#from collections import deque
num_lst = gen_num()

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
    len_left,len_right=len(left),len(right)
    i,j=0,0
    result =[]
    while i<len_left and j<len_right:
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    result +=left[i:]
    result +=right[j:]
    return result

print(merge_sort(num_lst))

