import  gen_num
num_lst = gen_num.gen_num1(10)
print(num_lst)
def insert_sort(A):
    length = len(A)
    for i in range(1,length):
        key = A[i]
        j = i
        while j>0 and A[j-1]>key:
            A[j]=A[j-1]
            j-=1
        A[j]=key
    return A
# print(insert_sort(num_lst))
def shell_sort(A):
    length = len(A)
    gaps = [8,4,2,1]
    for gap in gaps:
        if gap<length:
            for i in range(gap,length):
                key = A[i]
                j = i
                while j-gap>=0 and A[j-gap]>key:
                    A[j]=A[j-gap]
                    j-=gap
                A[j]=key
    return A
# print(shell_sort(num_lst))
def merge_sort(A):
    length = len(A)
    if length<=1:
        return A
    else:
        gid = length//2
        left = merge_sort(A[:mid])
        right = merge_sort(A[mid:])
        result = merge(left,right)
        return result
def merge(left,right):
    i,j = 0,0
    result = []
    while i<len(left)and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result+=left[i:]
    result+=right[j:]
    return result
# print(merge_sort(num_lst))
def tim_sort(A):
    new_run = [A[0]]
    runs = []
    result=[]
    for i in range(1,len(A)):
        if A[i-1]<A[i]:
            new_run.append(A[i])
        else:
            runs.append(new_run)
            new_run=[A[i]]
    runs.append(new_run)
    for run in runs:
        result = merge(result,run)
    return result
# print(tim_sort(num_lst))
def count_sort(A):
    min_value = min(A)
    max_value = max(A)
    count_lst = [0 for i in range(min_value,max_value+1)]
    for elem in A:
        count_lst[elem-min_value]+=1
    result = []
    for i in range(len(count_lst)):
        while count_lst[i]>0:
            result.append(i+min_value)
            count_lst[i]-=1
    return result
# print(count_sort(num_lst))
def radix_sort(A):
    length = len(str(max(A)))
    bucket = [[]for i in range(10)]
    for i in range(length):
        for elem in A:
            bucket[elem//pow(10,i)%10].append(elem)
        a = 0
        for buck in bucket:
            for num in buck:
                A[a]=num
                a+=1
    return A
# print(radix_sort(num_lst))
