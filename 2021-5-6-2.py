#import  gen_num
num1 = 21*99 
num2 = 21*5
c = num1%num2
c_lst = []
while c!=0:
    num1=num2
    num2=c
    c = num1%num2
    c_lst.append(c)
print(c_lst)
while True:
    x =  c_lst.pop()
    if x==0:
        result =  c_lst.pop()
        break
    else:
        break 
print(result)
