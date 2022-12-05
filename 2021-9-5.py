import  gen_num
num_lst = gen_num.gen_num1(10)
print(num_lst)

def bubble_sort(A):
    length = len(A)
    for i in reversed(range(1,length)):#[1,n-1]
        for j in range(i):
            if A[j]>A[j+1]:
                A[j],A[j+1]=A[j+1],A[j]
    return A
# print(bubble_sort(num_lst))
def select_sort(A):
    length = len(A)
    for i in reversed(range(1,length)):#[1,n-1]
        max_value = A[0]
        for j in range(i+1):
            max_value = max(max_value,A[j])
        max_idx = A.index(max_value)
        A[max_idx],A[j]=A[j],A[max_idx]
    return A
# print(select_sort(num_lst))

def binsearch(A,key):
    length = len(A)
    a = 0
    b = length-1
    if A[a]==key:
        return a
    if A[b]==key:
        return b
    while a<b:
        mid = (a+b)//2
        if A[mid]==key:
            return mid
        elif A[mid]>key:
            b = mid
        else:
            a = mid
    return -1
# print(binsearch(select_sort(num_lst),2))
num_lst = list(range(10))
a=0
b=len(num_lst)-1
def binsearch2(A,a,b,key):
    if A[a]==key:
        return a
    if A[b]==key:
        return b

    mid = (a+b)//2
    if A[mid]==key:
        return mid
    elif A[mid]>key:
        return binsearch2(A,a,mid,key)
    else:
        return binsearch2(A,mid,b,key)
    return -1
print(binsearch2(num_lst,a,b,2))

num_lst = gen_num.gen_num1(10) 
def quick_sort(A):
    length = len(A)
    if length<=1:
        return A
    else:
        key = A.pop()
        lesser,greater=[],[]
        for elem in A:
            if elem>key:
                greater.append(elem)
            else:
                lesser.append(elem)
        return quick_sort(lesser) + [key]+quick_sort(greater)
print(quick_sort(num_lst))
