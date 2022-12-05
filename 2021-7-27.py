import  gen_num
num_lst = gen_num.gen_num2(10)
print(num_lst)

def merge_sort(A):
    length = len(A)
    if length==1:
        return A
    else:
        mid = length//2
        left = merge_sort(A[:mid])
        right = merge_sort(A[mid:])
        return merge(left,right)

def merge(left,right):
    result = []
    i,j=0,0
    while i<len(left) and j <len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result += left[i:]
    result += right[j:]
    return result
print(merge_sort(num_lst))

