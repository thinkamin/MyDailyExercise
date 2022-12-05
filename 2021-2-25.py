'''
练习递归
'''
def func(n):
    if n == 0:
        return 1
    return n*func(n-1)
# for i in range(10):
    # print(func(i))

def fab(n):
    if n<3:return 1
    return fab(n-1)+fab(n-2)
for i in range(20):
    print(fab(i))

