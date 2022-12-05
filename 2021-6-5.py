key_lst = 'songyuanlong'
num_lst = range(12)
test_dict = dict(zip(num_lst,key_lst))
print(test_dict)
# help(sorted)
print(sorted(test_dict.items(),key = lambda kv:(kv[1],kv[0])))
print(test_dict)



