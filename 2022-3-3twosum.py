a = [2,7,11,15]
target= 9
def check(A,target):
    i=0
    j=len(a)-1
    while i<j:
        result = a[i]+a[j]
        if result <target:
            i+=1
        elif result>target:
            j-=1
        elif result==target:
            return a[i],a[j]
        else:
            return False,False

a,b=check(a,target)
print(a,b)


