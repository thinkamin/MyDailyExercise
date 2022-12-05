import  gen_num
num_lst = gen_num.gen_num1(10)
print(num_lst)

def merge_sort(A):
    length = len(A)
    if length<=1:
        return A
    else:
        mid = length//2
        left =  merge_sort(A[:mid]) 
        right =  merge_sort(A[mid:]) 
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

    result.extend(left[i:])
    result.extend(right[j:])
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
            new_run = [A[i]]
        else:
            new_run.append(A[i])
    runs.append(new_run)
    for run in runs:
        sorted_array = merge(sorted_array,run)
    return sorted_array

print(tim_sort(num_lst))


