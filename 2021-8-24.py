from statement import print11
print11()


def exchange(n):
    a = [10,5,1]
    n1 = n//10
    n2 = n%10//5
    n3 = n%5//1
    return n1,n2,n3,n1+n2+n3

for i in range(1,60):
    print(i,exchange(i))
