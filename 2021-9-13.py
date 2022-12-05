import  gen_num
num_lst = gen_num.gen_num1(10)
print(num_lst)
def bubble_sort(A):
    length = len(A)
    for i in reversed(range(1,length)):#[n-1,1]
        for j in range(i):
            if A[j]>A[j+1]:
                A[j],A[j+1]=A[j+1],A[j]
    return A
# print(bubble_sort(num_lst))
def select_sort(A):
    length=len(A)
    for i in reversed(range(1,length)):#[n-1,1]
        maxValue = A[0]
        for j in range(i+1):
            maxValue = max(maxValue,A[j])
        maxIdx = A.index(maxValue)
        A[maxIdx],A[j]=A[j],A[maxIdx]
    return A
# print(select_sort(num_lst))
s_lst = list(range(10))
def binsearch(A,key):
    a=0
    b=len(A)-1
    if A[a]==key:
        return a
    if A[b]==key:
        return b
    while a<b:
        mid = (a+b)//2
        if A[mid]==key:
            return mid
        elif A[mid]<key:
            a= mid
        else:
            b=mid
    return -1
# print(s_lst)
# print(binsearch(s_lst,5))
a = 0
b = len(s_lst)-1
def binsearch2(A,a,b,key):
    if A[a]==key:
        return a
    if A[b]==key:
        return b
    mid = (a+b)//2
    if A[mid]==key:
        return mid
    elif A[mid]<key:
        return binsearch2(A,mid,b,key)
    else:
        return binsearch2(A,a,mid,key)
    return -1
# print(binsearch2(s_lst,a,b,5))

def quick(A):
    length = len(A)
    if length<=1:
        return A
    else:
        key = A.pop()
        greater,lesser=[],[]
        for elem in A:
            if elem>key:
                greater.append(elem)
            else:
                lesser.append(elem)
        return quick(lesser)+[key]+quick(greater)
print(quick(num_lst))
