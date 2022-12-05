'''
max prizes
'''

def max_prizes(n):
    m = 1
    left = n-m
    result = []
    result.append(m)
    while left-m>0:
        m+=1
        left = left- m
        if left<=m:
            result.append(m+left)
            break
        else:
            result.append(m)
    return result
for i in range(1,200):
    print(i,max_prizes(i))
