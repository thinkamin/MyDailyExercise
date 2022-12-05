from my import gen_num
from collections import namedtuple
#from my import G1,G2
#from collections import deque
num_lst = gen_num()

def countsort(A):
    max_value = max(A)
    min_value = min(A)
    count_lst = [0 for i in range(min_value,max_value+1)]
    
    for item in A:
        count_lst[item-min_value]+=1
    result = []
    for i in range(len(count_lst)):
        while count_lst[i]>0:
            result.append(i+min_value)
            count_lst[i]-=1
    return result
print(countsort(num_lst))

def basesort(A):
    max_value=max(A)
    length = len(str(max_value))
    buck = [[] for i in range(10)]
    for i in range(length):
        for item in A:
            print("i,item:",i,item)
            buck[(item//(pow(10,i))%10)].append(item)
        print(i,buck)
        a=0
        for bucki in buck:
            for x in bucki:
                A[a]=x
                a+=1
                print('a:',a)
    return A
print((num_lst))

a = countsort(num_lst)
def binsearch(A,key):
    left=0
    right=len(A)
    while left<right:
        mid = (left+right)//2
        if A[mid]==key:
            return True,mid
        elif mid<key:
            left=mid+1
        else:
            right=mid-1
    return False
print(binsearch(a,5))

def binsearch2(A,key,left,right):
    if A[left]==key:
        return left
    if A[right]==key:
        return right
    mid = (left+right)//2
    print('mid:',mid)
    if left<right:
        if A[mid]==key:
            return True,mid
        elif A[mid]<key:
            left=mid
            return binsearch2(A,key,left,right)
        else:
            right=mid
            return binsearch2(A,key,left,right)
        return False

print(binsearch2(a,5,0,len(a)-1))



