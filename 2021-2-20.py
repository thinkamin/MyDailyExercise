'''
select sort upgrade
step1:循环n次 每次从1：n-1中找到largest
step2：交换位置
'''
import gen_num
num_lst = gen_num.gen_num1(20)
print(num_lst)
def select_sort(A):
    '''
    Args:
        A:num_lst
    '''
    length = len(A)
    for i in [length-x for x in range(length)]:#[length,1]
        largest = A[0]
        for item in A[1:i]:#[0:i-1]
            if item > largest:
                largest = item
        index = A.index(largest)
        
        A[index],A[i-1]=A[i-1],A[index]
    return A
print(select_sort(num_lst))


