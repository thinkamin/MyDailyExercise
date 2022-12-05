import  gen_num
num_lst = gen_num.gen_num1(10)
# print(num_lst)
def merge_sort(A):
    '''
    Args:
    A:num_lst
    '''
    length = len(A)
    if length == 1:
        return A
    mid = length//2
    left = merge_sort(A[:mid])
    right = merge_sort(A[mid:])
    return merge(left,right)
def merge(left,right):
    i,j=0,0
    result = []
    while i<len(left)and j<len(right):#ij[0,n-1]
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result+=left[i:]
    result+=right[j:]
    return result
print(merge_sort(num_lst))



