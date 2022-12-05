import math
def fab(n):
    if n<=1:
        return 1
    else:
        tables=[0 for _ in range(n+1)]
        tables[0]=1
        tables[1]=1
        for i in range(2,n+1):#[3,n]
            tables[i]=tables[i-1]+tables[i-2]
        return tables

# for i in range(10):
    # print(fab(i))

def coinchange(n):
    d = [1,3,4]
    tables = [math.inf for _ in range(n+1)]
    tables[0]=0
    for i in range(1,n+1):
        tables[i] = min(tables[i-3]+1,tables[i-1]+1,tables[n-4]+1)
    return tables

# for i in range(10,20):
    # print(i,coinchange(i)))

def calc(n):
    tables=[math.inf for _ in range(n+1) ]
    tables[0]=0
    tables[1]=1
    for i in range(2,n+1):
        if n%2==0 and n%3==0:
            tables[i]=min(tables[i//2]+1,tables[i//3]+1,tables[i-1]+1)
        if n%2!=0 and n%3==0:
            tables[i]=min(tables[n-1]+1,tables[n//3]+1)
        if n%2==0 and n%3!=0:
            tables[i]=min(tables[n-1]+1,tables[n//2]+1)
        if n%2!=0 and n%3!=0: 
            tables[i]=tables[i-1]+1

    return tables
for i in range(10,20):
    print(calc(i))
