import  gen_num
num_lst = gen_num.gen_num1(10)
print(num_lst)

def merge_sort(A):
    length = len(A)
    if length<=1:
        return A
    else:
        mid = length//2
        left = merge_sort(A[:mid])
        right = merge_sort(A[mid:])
        result = merge(left,right)
        return result
def merge(left,right):
    i,j=0,0
    result = []
    while i<len(left) and j<len(right):
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
def tim_sort(A):
    runs = []
    new_run =[A[0]]
    result = []
    length = len(A)
    for i in range(1,length):#[0,n-2]
        if A[i-1]<A[i]:
            new_run.append(A[i])
        else:
            runs.append(new_run)
            new_run = [A[i]]
    runs.append(new_run)
    for run in runs:
        result = merge(result,run)
    return result
print(tim_sort(num_lst))

def insert_sort(A):
    length = len(A)
    for i in range(1,length):#[1,n-1]
        key = A[i]
        j = i
        while A[j-1]>key and j>0:
            A[j]=A[j-1]
            j-=1
        A[j]=key
    return A
print(insert_sort(num_lst))

def shell_sort(A):
    length = len(A)
    gaps = [10,4,2,1]
    for gap in gaps:
        if gap<length:
            for i in range(gap,length):
                key = A[i]
                j = i 
                while A[j-gap]>key and j>0:
                    A[j] = A[j-gap]
                    j-=gap
                A[j]=key
    return A
print(shell_sort(num_lst))



