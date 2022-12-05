lst = [1,4,3,2]

def invertion_count(A):
    length = len(A)
    if length<=1:
        return A,0
    else:
        mid = length//2
        left,m=invertion_count(A[:mid])
        right,n=invertion_count(A[mid:]) 
        sorted_lst,p = total_count(left,right)
        return sorted_lst,m+n+p 

def total_count(left,right):
    i,j = 0,0
    result = []
    total=0
    while i<len(left) and j<len(right):
        if left[i]>right[j]:
            result.append(right[j])
            total+=len(left)-i
            j+=1
        else:
            result.append(left[i])
            i+=1

    result+=left[i:]
    result+=right[j:]
    return result,total
print(invertion_count(lst))
