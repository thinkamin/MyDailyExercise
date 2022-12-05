import  gen_num
num_lst = gen_num.gen_num1(10)
print(num_lst)

def bubble_sort(A):
    length = len(A)
    for i in reversed(range(1,length)):#[1,n-1]
        for j in range(i): 
            if A[j]>A[j+1]:
                A[j],A[j+1] = A[j+1],A[j]
    return A
# print(bubble_sort(num_lst))

def select_sort(A):
    length = len(A)
    for i in reversed(range(1,length)):#[1,n-1]
        max_value = A[0]
        for j in range(i+1):
            max_value = max(max_value,A[j])
        maxIdx = A.index(max_value)
        A[maxIdx],A[j] = A[j],A[maxIdx]
    return A
# print(select_sort(num_lst))
sorted_A = range(100)
a = 0
b = len(sorted_A)-1
def binsearch(A,a,b,key):
    if A[a]==key:
        return a
    if A[b]==key:
        return b
    mid = (a+b)//2
    if A[mid]==key:
        return mid
    elif A[mid]>key:
        return binsearch(A,a,mid,key)
    else:
        return binsearch(A,mid,b,key)
    return -1

print(binsearch(sorted_A,a,b,10))

def binsearch2(A,key):
    a = 0
    b = len(A)-1
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
print(binsearch2(sorted_A,10))


