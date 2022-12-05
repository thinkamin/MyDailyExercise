
'''
maximum advertisement revenue
'''
n = input('请输入每个序列的数量:')
s1 = input('请输入第一个序列的数字:')
s2 = input('请输入第二个序列的数字:')
n = int(n)
s1 = [int(i) for i in s1.split(',')]
s2 = [int(i) for i in s2.split(',')]
# print(s1,s2)
assert((n==len(s1))and(n==len(s2)))
sorted_s1 = sorted(s1)
sorted_s2 = sorted(s2)
s = 0
for i in range(n):
    s += sorted_s1[i]*sorted_s2[i]
print(s)

