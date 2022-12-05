import  gen_num
num_lst = gen_num.gen_num1(10)
print(num_lst)

def insert_sort(A):
    length = len(A)
    for i in range(1,length):#[1,n-1]
        key = A[i]
        j =i 
        while j>0 and A[j-1]>key:
            A[j]=A[j-1]
            j-=1
        A[j]=key
    return A
# print(insert_sort(num_lst))
def shell_sort(A):
    gaps = [10,8,4,1]
    length = len(A)
    for gap in gaps:
        if gap<length:
            for i in range(gap,length):
                key=A[i]
                j=i
                while j-gap>=0 and A[j-gap]>key:
                    A[j]=A[j-gap]
                    j-=gap
                A[j]=key
    return A
# print(shell_sort(num_lst))
def merge_sort(A):
    length = len(A)
    mid = length//2
    if length<=1:
        return A
    else:
        left=merge_sort(A[:mid])
        right=merge_sort(A[mid:])
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
    runs = []
    new_run=[A[0]]
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
def radix_sort(A):
    bucket = [[] for _ in range(10)]
    length = len(str(max(A)))
    for i in range(length):
        for elem in A:
            bucket[elem//(pow(10,i)%10)].append(elem)
        print(bucket)
        a = 0
        for buck in bucket:
            for n in buck:
                A[a]=n
                a+=1
    return A
print(radix_sort(num_lst))
            

