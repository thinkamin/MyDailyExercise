import  gen_num
num_lst = gen_num.gen_num1(10)
# print(num_lst)

def quick_sort(A):
    length = len(A)
    if length<=1:
        return A
    else:
        base = A.pop()
        greater,lesser = [],[]
        for item in A:
            if item>base:
                greater.append(item)
            else:
                lesser.append(item)
        return quick_sort(lesser)+[base]+quick_sort(greater)
print(quick_sort(num_lst))
