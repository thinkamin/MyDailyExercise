left = [1,3,5,7,9,11,20]
right = [2,4,6,8,10]

def merge(left,right):
    i,j=0,0
    result = []
    while i<len(left) and left[i]<right[j]:
        result.append(left[i])
        i+=1
    while j<len(right) and right[j]<left[i]:
        result.append(right[j])
        j+=1
    result +=left[i:]
    result +=left[j:]
    return result

a = merge(left,right)
print(a)


