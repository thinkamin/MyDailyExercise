import  gen_num
num_lst = gen_num.gen_num1(10)
print(num_lst)

def quicksort(A):
    '''
    Args:
    A:num_lst
    '''
    length = len(A)
    if length <=1:#重点关注
        return A
    base = A.pop()
    lesser,greater=[],[]
    for num in A:
        if num >base:
            greater.append(num)
        else:
            lesser.append(num)
    return quicksort(lesser)+[base]+quicksort(greater)
print(quicksort(num_lst))

