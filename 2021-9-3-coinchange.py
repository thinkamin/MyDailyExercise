import math

def coin_change(n):
    d = [1,3,4]
    tables = [math.inf for i in range(n+1)]#[0,n]
    tables[0]=0
    for i in range(1,n+1):#[1,n]
        tables[i] = min(tables[i-1]+1,tables[i-3]+1,tables[i-4]+1)#i-4=-1 i>3
        # print(i)
    return tables
for i in range(3,25):#i>=3 i-4才有意义
    print(coin_change(i))
