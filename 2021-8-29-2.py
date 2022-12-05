import  gen_num
num_lst = gen_num.gen_num1(10)
print(num_lst)

def quick_sort(A):
    length = len(A)
    if length<=1:
        return A
    else:
        key = A.pop()
        lesser,greater = [],[]
        for elem in A:
            if elem>key:
                greater.append(elem)
            else:
                lesser.append(elem)
        return quick_sort(lesser)+[key]+quick_sort(greater)
# print(quick_sort(num_lst))
def count_sort(A):
    length = len(A)
    maxValue = max(A)
    minValue = min(A)
    count_lst = [0 for i in range(minValue,maxValue+1)]
    for elem in A:
        count_lst[elem-minValue]+=1

    result = []
    for i in range(len(count_lst)):
        while count_lst[i]>0:
            result.append(i+minValue)
            count_lst[i]-=1
    return result
# print(count_sort(num_lst))
    
def radix_sort(A):
    maxValue = max(A)
    length = len(str(maxValue))# 123->3
    radix = 10
    bucket = [[]for i in range(radix)]
    for i in range(length):#[0,n-1]
        for elem in A:
            bucket[elem//pow(radix,i)%radix].append(elem)
        # print(i,bucket)
        a = 0 
        for buck in bucket:
            for elem2 in buck:
                A[a] = elem2
                a+=1
    return A
print('song',radix_sort(num_lst))
    


