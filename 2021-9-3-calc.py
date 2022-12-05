import math

def calc(n):
    tables = [math.inf for i in range(n+1)] #[0,n]
    tables[0]=0
    for i in range(1,n+1):
        if i%2==0 and i%3!=0 :
            tables[i] = min(tables[i-1]+1,tables[i//2]+1)
        if i%3==0 and i%2!=0:
            tables[i] = min(tables[i-1]+1,tables[i//3]+1)
        if i%2==0 and i%3==0:
            tables[i] = min(tables[i-1]+1,tables[i//2]+1,tables[i//3]+1)
        if i%2!=0 and i%3!=0:
            tables[i] = tables[i-1]+1
        # print(i,tables)
    return tables
for i in range(4,10):#[0,9]
    print(i,calc(i))


'''
8 = 0+1*3+1+1 result:4
9 = 0+1*3*3   result:3
'''
