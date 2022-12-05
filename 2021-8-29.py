num_lst = [2,2,2,3,4]

def insert_sort(A):
    length = len(A)
    for i in range(1,length):#[1,n-1]
        key = A[i]
        j = i
        while A[j-1]>key:
            A[j]=A[j-1]
            j-=1
        A[j]=key
    return A

def check(A):
    sorted_lst = insert_sort(A)
    length = len(A)
    mid = length//2
    key = A[mid]
    left_n = count_key(A[:mid],key)
    right_n = count_key(A[mid:],key)
    total = left_n+right_n
    if total>length/2:
        return 1
    else:
        return -1


def count_key(num_lst,key):
    count = 0
    for key in num_lst:
        count+=1
    return count

print(check(num_lst))



