import  gen_num
num_lst = gen_num.gen_num1(10)
print(num_lst)

def quick_sort(A):
    if len(A)<=1:
        return A
    else:
        base = A.pop()
        lesser,greater = [],[]
        for item in A:
            if item < base:
                lesser.append(item)
            else:
                greater.append(item)
        return quick_sort(lesser)+[base]+quick_sort(greater)

print(quick_sort(num_lst))
