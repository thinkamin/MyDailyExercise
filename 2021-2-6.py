#bubble sort
import random

num_list = list(range(10))#[0,9]
random.shuffle(num_list)
print(num_list)

def bubbleSort(A):
    length = len(A)
    for i in range(length):#[0,9]
        length2 = len(A)
        for j in range(length2-1):#[0,8] [0,7]
            if A[j]>A[j+1]:
                A[j],A[j+1]=A[j+1],A[j]
        length2 -=1
    print(A)
bubbleSort(num_list)




