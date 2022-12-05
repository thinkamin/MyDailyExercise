#medianSort
import math
import numpy as np
import random
num_list = list(range(11))
random.shuffle(num_list)
print('origin list:',num_list)

def medianSort(A,left,right):
    '''
    Args:
        A:number list
        left:left index
        right:right index
    '''
    if left < right:
        median = np.median(A[left:right+1]) 
        print(median)
        med_index = A.index(median)
        mid = math.floor((left+right)/2)
        A[med_index],A[mid]=A[mid],A[med_index]
        for i in range(left,mid):
            if A[i]>A[mid]:
                for k in range(mid+1,right+1):
                    if A[k]<A[mid]:
                        A[i],A[k]=A[k],A[i]
                        break
        print(num_list)
        medianSort(A,left,mid-1)
        medianSort(A,mid+1,right)
medianSort(num_list,0,10)
# print(num_list)

