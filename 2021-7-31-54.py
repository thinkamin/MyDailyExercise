a = 123
b = 9
c = 4
num_lst = [a,b,c]
def max_concennate(A):
    radix = 10
    f_lst = []
    for item in A:
        m = len(str(item))
        m = m-1
        first_digit = item//pow(radix,m)%10 
        f_lst.append(first_digit)
    f_dict = dict(zip(f_lst,A))
    result =[]
    for k,v in reversed(sorted(f_dict.items())):
        result.append(v) 
    return result
print(max_concennate(num_lst))

