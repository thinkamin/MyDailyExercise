# from my import gen_num
# from collections import namedtuple
#from my import G1,G2
#from collections import deque
# num_lst = gen_num()


def infix2postfix(string):
    print(string)
    p_dict={
            '+':1,
            '-':1,
            '*':2,
            '/':2,
            '(':0
            }
    operator_list =[]
    result = []
    for i,item in enumerate(string):
        print("step",i,item)
        if item == '(':
            operator_list.append(item)
            print(operator_list)
        elif item ==')':
            while operator_list:
                u = operator_list.pop()
                if u !='(':
                    result.append(u)
                else :
                    break
            print(operator_list)
        elif item in list(['+','-','*','/']):
            if operator_list:
                v = operator_list[-1]
                if p_dict[item]>p_dict[v]:
                    operator_list.append(item)
                    # print(operator_list)
                else:
                    z = operator_list.pop()
                    # print(operator_list)
                    result.append(z)
                    operator_list.append(item)
                    # print(operator_list)
            else:
                operator_list.append(item)
            print(operator_list)
        else:
            result.append(item)
    # print(operator_list)
    while operator_list:
        u = operator_list.pop()
        result.append(u)
    return result


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
            value = calc(op2,op,op1)
            result.append(value)
    result = result.pop()
    return result

string='(3-2)*(4+5)/2'
a = infix2postfix(string)
print(a)
result = calcpost(a)
print(string)
print(result)
