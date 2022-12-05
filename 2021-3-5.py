import gen_num
num_lst = gen_num.gen_num1(10)
print(num_lst)

def buildheap(A):
    '''
    Args:
    A:num_lst
    '''
    length = len(A)
    mid = length//2-1
    for i in [mid-x for x in range(1,mid+1)]:#[mid,0]
        heapify(A,i,length-1)

def heapify(A,idx,maxIdx):
    left = 2*idx+1
    right = 2*idx+2
    if left<maxIdx and A[left]>A[idx]:
        largest = left
    else:
        largest = idx
    if right<maxIdx and A[right]>A[largest]:
        largest = right
    if largest != idx:
        A[idx],A[largest]=A[largest],A[idx]
        heapify(A,largest,maxIdx)

def heapsort(A):
    '''
    args:
    a:num_lst
    '''
    length = len(A)
    buildheap(A)
    for i in [length-1-x for x in range(length)]:#[n-1,0]
        A[0],A[i]=A[i],A[0]
        #根节点的左右孩子也是第2第3大的 把最底层的一个换到根节点 肯定会触发largest!=idx
        heapify(A,0,i)#make mistake
        print(i,A)
    return A

print(heapsort(num_lst)) 
