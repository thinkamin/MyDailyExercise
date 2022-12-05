# from my import gen_num
# from collections import namedtuple
#from my import G1,G2
#from collections import deque
# num_lst = gen_num()
def calc(n):
    if n<=1:
        return n
    else:
        return n*calc(n-1)
# print(calc(3))
