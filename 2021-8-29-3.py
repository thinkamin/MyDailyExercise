
def fab(n):
    if n<=1:
        return 1
    else:
        return fab(n-1)+fab(n-2)
for i in range(40):
    print(i,fab(i))
