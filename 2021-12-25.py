from myutils import gen_num

num_lst = gen_num()
print('origin_lst',num_lst)

def insert_sort(A):
    length = len(A)
    for i in range(1,length):#1,n-1
        key = A[i]
        j = i
        while A[j-1]>key and j>0:
            A[j]=A[j-1]
            j=j-1
        A[j]=key
    return A
print('insert_sort',insert_sort(num_lst))

def shell_sort(A):
    length = len(A)
    gaps = [8,4,2,1]
    for gap in gaps:
        if gap<length:
            for i in range(gap,length):#gap,n-1
                key = A[i]
                j = i
                while A[j-gap]>key and j>gap-1:
                    A[j]=A[j-gap]
                    j = j-gap
                A[j]=key
    return A
print('shell_sort',shell_sort(num_lst))

def merge_sort(A):
    length = len(A)
    if length<=1:
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
    result+=left[i:]
    result+=right[j:]
    return result
print('merge_sort',merge_sort(num_lst))

def tim_sort(A):
    runs = []
    new_run=[A[0]]
    result=[]
    length = len(A)
    for i in range(1,length):#1,n-1
        if new_run[-1]<A[i]:
            new_run.append(A[i])
            i+=1
        else:
            runs.append(new_run)
            new_run=[A[i]]
    runs.append(new_run)
    for run in runs:
        result=merge(result,run)
    return result
print('tim_sort',tim_sort(num_lst))

def quick_sort(A):
    length=len(A)
    if length<=1:
        return A
    else:
        lesser,larger = [],[]
        key = A.pop()
        for item in A:
            if item<key:
                lesser.append(item)
            else:
                larger.append(item)
        return quick_sort(lesser)+[key]+quick_sort(larger)
print('quick_sort',quick_sort(num_lst))


