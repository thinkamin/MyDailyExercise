import  gen_num
num_lst = gen_num.gen_num2(10)
print(num_lst)

def count_sort(A):
    max_value = max(A)
    min_value = min(A)
    count_lst = [0 for i in range(min_value,max_value+1)]#[min_value,max_value]
    for elem in A:
        count_lst[elem-min_value]+=1
    print(count_lst)
    result = []
    for i in range(len(count_lst)):
        while count_lst[i]>0:
            result.append(i+min_value)
            count_lst[i]-=1
    return result
print(count_sort(num_lst))


def radix_sort(A):
    max_value = max(A)
    n = len(str(max_value))
    for i in range(0,n):#[0,n-1]
        bucket = [[] for i in range(10)]
        for elem in A:
            bucket[elem//pow(10,i)%10].append(elem)
        print(i,bucket)
        
        a = 0 
        for buck in bucket:
            for i in buck:
                A[a]=i
                a+=1
    return A
print(radix_sort(num_lst))


