
ip = '192.168.1.1'
mask = '255.255.192.0'
ip_lst = list(map(int,ip.split('.')))
# print(ip_lst)
mask_lst = list(map(int,mask.split('.')))
# print(mask_lst)
result = []
for i in range(len(ip_lst)):
    result.append(ip_lst[i]&mask_lst[i])
print(result)


