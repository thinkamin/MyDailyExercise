import  gen_num
num_lst = gen_num.gen_num1(10)
print(num_lst)


def buildheap(A):
    length = len(A)
    for i in reversed(range(length//2)):
        heapify(A,i,length)

def heapify(A,idx,maxIdx):
    left = 2*idx+1
    right = 2*idx+2
    if right<maxIdx and  A[right]>A[idx]:
        largest = right
    else:
        largest = idx
    if left<maxIdx and  A[left]>A[largest]:
        largest = left
    # print(largest)
    if largest!=idx:
        A[idx],A[largest] = A[largest],A[idx]
        heapify(A,largest,maxIdx)

            
result = []
buildheap(num_lst)
for i in range(len(num_lst)):#[0,n-1]
    key = num_lst.pop(0) 
    print(num_lst)
    result.append(key)
    buildheap(num_lst)
print(result)


