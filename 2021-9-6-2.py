

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
# print(insert_sort(num_lst))

def radix_sort(A):
    gaps = [10,8,4,1]
    length = len(A)
    for gap in gaps:
        if gap<length:
            for i in range(gap,length):
                # print('i',i)
                key=A[i]
                j = i
                while A[j-gap]>key and j-gap>=0:
                    A[j]=A[j-gap]
                    j-=gap
                A[j]=key
    return A
# print(radix_sort(num_lst))

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
    runs=[]
    new_run=[A[0]]
    result = []
    for i in range(1,len(A)):
        if A[i]>A[i-1]:
            new_run.append(A[i])
        else:
            runs.append(new_run) 
            new_run=[A[i]]
    runs.append(new_run)
    print(runs)
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
    result=[]
    for i in range(len(count_lst)):
        while count_lst[i]>0:
            result.append(i+min_value)
            count_lst[i]-=1
    return result
# print(count_sort(num_lst))
def base_sort(A):
    length = len(str(max(A)))
    bucket = [[]for i in range(10)]
    for i in range(length):
        for elem in A:
            bucket[(elem//(pow(10,i))%10)].append(elem)
        a = 0 
        for buck in bucket:
            for i in buck:
                A[a]=i
                a+=1
    return A
# print(base_sort(num_lst))
