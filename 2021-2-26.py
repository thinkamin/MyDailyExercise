'''
build heap
'''
import gen_num

num_lst = gen_num.gen_num1(10)
print(num_lst)


def buildheap(A):
    length = len(A)
    i = int((length)/2-1) #这是关键
    maxIdx = length-1
    for j in [i-x for x in range(0,i+1)]:#[i,0]
        heapify(A,j,maxIdx)
        print(j,A)
    return A

def heapify(A,idx,maxIdx):
    left = 2*idx + 1
    right = 2*idx +2
    if left<maxIdx and A[left]>A[idx]:
        A[left],A[idx] = A[idx],A[left]
    if right<maxIdx and A[right]>A[idx]:
        A[right],A[idx] = A[idx],A[right]


result = buildheap(num_lst)  
print(result) #满足最大的在最上面  但其他的父亲就不一定了

