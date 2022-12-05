#money change
import random
d = [10,5,1]
def money():
    n = random.randint(1,1000)
    return n
def money_change(n):
    global d
    a = n//d[0]
    b  = (n-a*d[0])//d[1]
    c = (n-a*d[0]-b*d[1])//d[2]
    return a+b+c

def money_change2(n):
    global d
    return n//d[0]+n%d[0]//d[1]+n%d[1]//d[2]


for i in range(10):
    n = money()
    print(n,money_change(n),money_change2(n))


