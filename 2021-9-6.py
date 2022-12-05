import math
n = 3
backpack = 10
w = 1,4,8
def max_gold(n):
    tables = [-math.inf for i in range(n+1) ]
    tables[0]=0
    for i in range(1,n):
        tables[i] = max(tables[i-1]+1,tables[i-4]+4,tables[i-8]+8)
    return tables[n-1]
print(max_gold(10))
