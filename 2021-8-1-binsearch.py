num_lst = list(range(10))
print(num_lst)

def binsearch(A,key):
    minIdx = 0
    maxIdx =len(A)-1
    while minIdx<maxIdx:
        midIdx = (minIdx+maxIdx)//2
        if A[midIdx]==key:
            return midIdx
        elif A[midIdx]<key:
            minIdx = midIdx+1
        else:
            maxIdx = midIdx+1
    return -1

print(binsearch(num_lst,2))
