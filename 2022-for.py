from my import gen_num
from collections import namedtuple
#from my import G1,G2
#from collections import deque
num_lst = gen_num()
print(num_lst)
num_lst2 = sorted(num_lst)
print(num_lst2)
length = len(num_lst2)
for i in range(length):
    for j in range(i+1,length):
        for k in range(j+1,length):
            print(i,j,k,num_lst2[i]+num_lst2[j]+num_lst2[k])
