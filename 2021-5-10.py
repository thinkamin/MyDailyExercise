import  gen_num

num_lst = gen_num.gen_num1(10)
print(num_lst)

def merge_sort(A):
    '''
    Args:
    A:num_lst
    '''
    length = len(A)#length minum 1
    if length ==1:
        return A
    else:
        mid = length//2
        left = merge_sort(A[:mid])
        right = merge_sort(A[mid:])
        return merge(left,right)
def merge(left,right):
    i,j = 0,0
    result = []
    #一个列表迭代完成 停止
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    if i==len(left):
        result+=right[j:]
    else:
        result+=left[i:]
    return result
print(merge_sort(num_lst))
