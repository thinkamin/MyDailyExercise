from my import gen_num
from collections import namedtuple
#from my import G1,G2
#from collections import deque
num_lst = gen_num()

def insertSort(A):
    length = len(A)
    for i in range(1,length):
        j = i
        key = A[j]
        while j-1>=0 and A[j-1]>key:
            A[j]=A[j-1]
            j-=1
        A[j]=key
    return A
print(insertSort(num_lst))

def timSort(A):
    new_run=[A[0]]
    runs=[]
    for i in range(1,len(A)):
        if A[i-1]<A[i]:
            new_run.append(A[i])
        else:
            runs.append(new_run)
            new_run=[]
            new_run.append(A[i])
    runs.append(new_run)
    
    result = []
    for run in runs:
        result =merge(result,run)
    return result

def merge(left,right):
    ll = len(left)
    lr = len(right)
    i,j=0,0
    result=[]
    while i<ll and j<lr:
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    result+=left[i:]
    result+=right[j:]
    return result
print(timSort(num_lst))

def baseSort(A):
    length = len(str(max(A)))
    
    for i in range(length):
        count_lst = [[]for i in range(10)]
        for item in A:
            x = item//pow(10,i)%10
            count_lst[x].append(item)

        print("i,count:",i,count_lst)
        a = 0 
        for buck in count_lst:
            for i in buck:
                A[a]=i
                a+=1
        count_lst.clear()
    return A
print(baseSort(num_lst))

def buildHeap(A,idx,maxId):
    left = 2*idx+1
    right= 2*idx+2
    if right<maxId:
        pass
        
    
    if idx!=largest:
        buildHeap(A,largest,maxId)


num_lst = gen_num()
print(num_lst)
def quickSort(A):
    length = len(A)
    if length<=1:
        return A
    else:
        key = A.pop()
        lesser,greater=[],[]
        for item in A:
            if item<key:
                lesser.append(item)
            else:
                greater.append(item)
        return quickSort(lesser)+[key]+quickSort(greater)
print("result",quickSort(num_lst))
