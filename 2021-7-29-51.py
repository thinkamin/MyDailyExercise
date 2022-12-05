'''
Money Change
'''
import random
d = [10,5,1]

def moneychange(n):
    global d
    a = n//d[0]
    b = n%d[0]//d[1]
    c = n%d[1]//d[2]
    print('{}:{}个{},{}个{}，{}个{}'.format(n,a,d[0],b,d[1],c,d[2]))
    return a+b+c

for i in range(10):
    n = random.randint(1,10000)
    moneychange(n)
