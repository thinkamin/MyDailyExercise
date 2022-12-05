from my import gen_num
from collections import namedtuple
num_lst = gen_num()
print(num_lst)

def count_sort(A):
    min_value = min(A)
    max_vlaue = max(A)
    count_lst = [0 for i in range(min_value,max_vlaue+1)]

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


def base_sort(A):
    length = len(str(max(A)))
    bucket = [ [] for i in range(10)]
    for i in range(length):
        for elem in A:
            bucket[(elem//(pow(10,i))%10)].append(elem)

        a = 0
        for buck in bucket:
            for i in buck:
                A[a]=i
                a+=1
    return A
print(base_sort(num_lst))

