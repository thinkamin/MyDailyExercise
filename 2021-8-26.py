#很经典的递归和while的转换
num_lst = list(range(10))
print(num_lst)

a = 0 
b = len(num_lst)-1
#递归
def binsearch(A,a,b,key):
    if A[a]==key:
        return a
    if A[b]==key:#所有端点值要单独拿出来考虑
        return b
    if a<b:
       mid = (a+b)//2#向左取整会有个bug 永远到不了b
       # print(mid)
       if A[mid]==key:
           return mid
       elif A[mid]>key:
           return binsearch(A,a,mid,key)
       else:
           return binsearch(A,mid,b,key)
    return -1

# for i in range(10):
    # print(binsearch(num_lst,a,b,i))
# print(binsearch(num_lst,a,b,8))
def binsearch2(A,key):
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
        elif A[mid]<key:
            a = mid 
        else:
            b =mid
    return -1
for i in range(10):
    print(binsearch(num_lst,a,b,i))
