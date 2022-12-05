#select sort
import random

num_list = list(range(10))#[0,9]
random.shuffle(num_list)
# print(num_list)
def selectMax(A,left,right):
    maxPos = left
    i = left
    for i in range(left,right+1):#[left,right] 
        if A[i]>A[maxPos]:
            maxPos = i
    # print('maxPos',maxPos)
    return maxPos

def sortPointers(A):
    length=len(A)
    for i in [length-x for x in range(1,length)]:#[n-1,1]
        maxPos = selectMax(A,0,i)#0-i之间的最大值的索引
        if maxPos != i:
            A[i],A[maxPos] = A[maxPos],A[i]
sortPointers(num_list)

print(num_list)

