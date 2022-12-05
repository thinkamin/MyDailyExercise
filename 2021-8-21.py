import  gen_num
num_lst = gen_num.gen_num1(10)
print(num_lst)


def merge_sort(A):
    length = len(A)
    if length <=1:
        return A
    else:
        mid = length//2
        left = merge_sort(A[:mid])
        right = merge_sort(A[mid:])
        return merge(left,right)
def merge(left,right):
    i,j=0,0
    result = []
    while i<len(left)and j<len(right):
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


def tim_sort(A):
    length = len(A)
    runs = []
    new_run = [A[0]]
    sorted_array = []
    for i in range(1,length):#[1,n-1]
        if A[i-1]>A[i]:
            runs.append(new_run)
            new_run=[A[i]]
            print('new_run',new_run)
        else:
            new_run.append(A[i])
            print('new_run',new_run)
    runs.append(new_run)#重点
    # print('runs',runs)
    for run in runs:
        sorted_array = merge2(sorted_array,run)
    return sorted_array
def merge2(left,right):
    if not left:
        return right
    if not right:
        return left
    if left[0]<right[0]:
        return [left[0]]+merge2(left[1:],right)
    else:
        return [right[0]]+merge2(left,right[1:])


print(tim_sort(num_lst))
