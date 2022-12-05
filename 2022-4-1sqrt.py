
def sqrt(num):
    left=1
    right=num
    
    while left<=right:
        mid = (left+right)/2
        sqrt = num/mid
        if sqrt-mid<0.001:
            return mid
        elif mid>sqrt:
            right=mid

        elif mid<sqrt:
            left=mid
