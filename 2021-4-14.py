# 转为后缀表达式.运算表达式元素之间用空格隔开:
def change_houzhui(s):
    result = []  # 结果列表
    stack = []  # 栈
    s_lt = s.split(' ')
    for item in s_lt:
        if item.isnumeric():  # 如果当前字符为数字那么直接放入结果列表
            result.append(item)
        else:  # 如果当前字符为一切其他操作符
            if len(stack) == 0:  # 如果栈空，直接入栈
                stack.append(item)
            elif item in '*/(':  # 如果当前字符为*/（，直接入栈
                stack.append(item)
            elif item == ')':  # 如果右括号则全部弹出（碰到左括号停止）
                t = stack.pop()
                while t != '(':
                    result.append(t)
                    t = stack.pop()
            # 如果当前字符为加减且栈顶为乘除，则开始弹出
            elif item in '+-' and stack[-1] in '*/':
                if stack.count('(') == 0:  # 如果没有左括号，弹出所有
                    while stack:
                        result.append(stack.pop())
                else:  # 如果有左括号，弹到左括号为止
                    t = stack.pop()
                    while t != '(':
                        result.append(t)
                        t = stack.pop()
                    stack.append('(')
                stack.append(item)  # 弹出操作完成后将‘+-’入栈
            else:
                stack.append(item)  # 其余情况直接入栈（如当前字符为+，栈顶为+-）

    # 表达式遍历完了，但是栈中还有操作符不满足弹出条件，把栈中的东西全部弹出
    while stack:
        result.append(stack.pop())
    # 返回字符串
    return result

#后缀表达式进行计算
def calac_houzhui(follow):
    num = []
    base_opt = ['+', '-', '*', '/']
    for j in follow:
        if j.isdigit():
            num.append(int(j))
        if j in base_opt:
            num2 = num.pop()
            num1 = num.pop()
            if j == "+":
                num.append(num1 + num2)
            elif j == "-":
                num.append(num1 - num2)
            elif j == "*":
                num.append(num1 * num2)
            else:  
                num.append(num1 / num2)
    return num
if __name__ == '__main__':
    s = "9 + 3 * ( 2 + 1 )"   #空格隔开,括号注意中英文不要乱
    print(calac_houzhui(change_houzhui(s)))
