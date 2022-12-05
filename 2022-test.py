from my import gen_num
from collections import namedtuple
#from my import G1,G2
#from collections import deque
num_lst = gen_num()

string_test= "(12314)("
result =[]
for i in string_test:
    if i=='(':
        result.append(i)
    if i==')':
        result.pop()
if len(result):
    print("failure")

