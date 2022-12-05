import itertools as it 

print(list((it.product('ABCD',repeat=2))))
print('*'*10)
per_lst  =list((it.permutations('ABCD',2)))
print(len(per_lst))
com_lst  = list(it.combinations('ABCD',2))
print(com_lst)
print(len(com_lst))
com2_lst = list(it.combinations_with_replacement('ABCD',2))
print(com2_lst)
print(len(com2_lst))
