def fab(n):
    tables = [0 for i in range(n)]#n个
    tables[0],tables[1]=1,1
    for i in range(3,n):#3,n-1
        tables[i-1]=tables[i-2]+tables[i-3]
        print(tables)
    return tables[n-2]
for i in range(3,10):
    print(fab(i))
