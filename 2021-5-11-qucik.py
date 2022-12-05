import  gen_num
num_lst = gen_num.gen_num1(100)
# print(num_lst)

def quick_sort(A):
    '''
    Args:
    A;num_lst
    '''
    length = len(A)
    if length <=1:#可能为0 
        return A
    else:
        base = A.pop()
        lesser,greater = [],[]
        for num in A:
            if num>base:
                greater.append(num)
            else:
                lesser.append(num)
        return quick_sort(lesser)+[base]+quick_sort(greater)
print(quick_sort(num_lst))

