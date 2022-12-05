from my import gen_num

num_lst = gen_num()

def bubble_sort(A):
    length = len(A)
    for i in range(length):#0,n-1
        for j in range(1,length):#1,n-1
            if A[j-1]>A[j]:
                A[j-1],A[j]=A[j],A[j-1]
    return A
# print(bubble_sort(num_lst))

def select_sort(A):
    length=len(A)
    for i in reversed(range(length)):#0,n-1
        max_num = A[0]
        for j in range(i+1):#0,i
            max_num = max(A[j],max_num)
        max_idx = A.index(max_num)
        A[j],A[max_idx]=A[max_idx],A[j]
    return A
# print(select_sort(num_lst))
def quick_sort(A):
    length = len(A)
    if length<=1:
        return A
    else:
        key = A.pop()   
        greater,lesser = [],[]
        for item in A:
            if item<key:
                lesser.append(item)
            else:
                greater.append(item)
        return quick_sort(lesser)+[key]+quick_sort(greater)
# print(quick_sort(num_lst))

def count_sort(A):
    max_num = max(A)
    min_num = min(A)
    count_lst = [0 for i in range(min_num,max_num+1)]
    for item in A:
        count_lst[item-min_num]+=1
    result =[]
    for idx in range(len(count_lst)):
        while count_lst[idx]>0:
            result.append(min_num+idx)
            count_lst[idx]-=1
    return result
# print(count_sort(num_lst))


# def bucket_sort(A):

