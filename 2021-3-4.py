import gen_num

num_lst = gen_num.gen_num1(20)
# print(num_lst)
def mergesort(A):
    '''
    Args:
    A:num_lst
    '''
    if len(A) == 1:
        return A
    mid = len(A)//2
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
            j +=1
    result+=left[i:]
    result+=right[j:]
    return result

print(mergesort(num_lst))
