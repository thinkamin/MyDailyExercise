# import  gen_num

# num_lst = gen_num.gen_num1(10)
# print(num_lst)
n1 = 21*13
n2 = 21*8
def func(n1,n2):
    c = n1%n2
    if c == 0:
        return c
    print(c)
    return func(n2,c)
print(func(n1,n2))
