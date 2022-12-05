# from my import gen_num
# from collections import namedtuple
#from my import G1,G2
#from collections import deque
# num_lst = gen_num()
# recuise

#阶乘
def func(n):
    if n==0:
        return 1
    if n>=1:
        return func(n-1)*n
for i in range(20):
    print('{}的阶乘:'.format(i),func(i))

        
