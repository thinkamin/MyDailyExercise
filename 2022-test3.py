# from my import gen_num
# from collections import namedtuple
#from my import G1,G2
#from collections import deque
# num_lst = gen_num()
string="52/4+5*2+"


def calc(op1,op,op2):
    op1 = int(op1)
    op2 = int(op2)
    if op=='+':
        return op1+op2
    if op=='-':
        return op1-op2
    if op=='*':
        return op1*op2
    if op=='/':
        return op1/op2



def calcpost(string):
    result = []
    for item in string:
        if item in str(list('1234567890')):
            result.append(item)
        else:
            op1 = result.pop()
            op2 = result.pop()
            op = item 
            value = calc(op1,op,op2)
            result.append(value)
    result = result.pop()
    return result

result = calcpost(string)
print(result)
