from my import gen_num
from collections import namedtuple
#from my import G1,G2
#from collections import deque
num_lst = gen_num()


def quickSort(A):
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
        return quickSort(lesser)+[key]+quickSort(greater)
print(quickSort(num_lst))

def quickSort(A,left,right):
    if right <=left:
        return 
    a = i = left
    b = right
    pivot = A[left]
    while i <= b:
        print('i:{},b:{},A:{}'.format(i,b,A))
        # print(A)
        if A[i] < pivot:
            A[a],A[i] = A[i],A[a]
            a += 1
            i += 1
        elif A[i] > pivot:
            A[b],A[i] = A[i],A[b]
            b -= 1
        else:
            i += 1
    quickSort(A,left,a-1)
    quickSort(A,b+1,right)
print(quickSort(num_lst,0,len(num_lst)-1))


