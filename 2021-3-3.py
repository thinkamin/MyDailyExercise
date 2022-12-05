import gen_num

num_lst = gen_num.gen_num1(20)
'''
def merge(left,right):
    i,j=0,0
    result = []
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i +=1 #多运行了一次
        if left[i]>right[j]:
            result.append(right[j])
            j+=1
    result +=left[i:]
    result +=right[j:]
    print(result)
    return result
'''
def mergesort(A):
    '''
    Args:
    A;num_lst
    '''
    length = len(A)
    if length == 1:
        return A
    mid = length//2
    left = mergesort(A[:mid])
    right = mergesort(A[mid:])
    return merge(left,right)
def merge(left,right):
    i,j=0,0
    result = []
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i +=1
        else:    
            result.append(right[j])
            j+=1
    result +=left[i:]
    result +=right[j:]
    return result

left = [1,3,5] 
right = [2,4,6]
print(merge(left,right))
print(mergesort([1,5,4,2,6,10,9]))
