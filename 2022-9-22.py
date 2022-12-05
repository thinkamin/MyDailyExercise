from my import gen_num
from collections import namedtuple
#from my import G1,G2
#from collections import deque
num_lst = gen_num()

def quick_sort(A):
    length = len(A)
    if length<=1:
        return A
    else:
        key = A.pop()
        lesser,greater=[],[]
        for item in A:
            if item<key:
                lesser.append(item)
            else:
                greater.append(item)
        return quick_sort(lesser)+[key]+quick_sort(greater) 

# print(quick_sort(num_lst))

def tim_sort(A):
    new_run = [A[0]]
    runs = []
    for item in A:
        if item>new_run[-1]:
            new_run.append(item)
        else:
            runs.append(new_run)
            new_run = []
            new_run.append(item)
    runs.append(new_run)
    print(runs)
    result = []
    for run in runs:
        result=merge(result,run)
    return result



def merge(left,right):
    left_len,right_len = len(left),len(right)
    i,j=0,0
    result = []
    while i<left_len and j<right_len:
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result += left[i:]
    result += right[j:]
    return result

print(tim_sort(num_lst))        

            
