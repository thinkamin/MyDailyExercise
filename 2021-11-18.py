import  gen_num
num_lst = gen_num.gen_num1(10)
print(num_lst)

def quick_sort(A):
    length = len(A)
    if length<=1:
        return A
    else:
        key = A.pop()
        lesser,greater=[],[]
        for item in A:
            if item>key:
                greater.append(item)
            else:
                lesser.append(item)
        print(lesser,greater)
        return quick_sort(lesser)+[key]+quick_sort(greater)

print(quick_sort(num_lst))
