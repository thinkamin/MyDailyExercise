import  gen_num
# num_lst = gen_num.gen_num1(10)
# print(num_lst)
num_lst = [1,4,1,2]
def inversion(A):
    length = len(A)
    if length<=1:
        return A,0
    else:
        mid = length//2
        left,m=inversion(A[:mid])
        right,n=inversion(A[mid:])
        result,p = merge_count(left,right)
        return result,m+n+p

def merge_count(left,right):
    i,j=0,0
    result=[]
    num = 0
    while i<len(left)and j<len(right):
        if left[i]>=right[j]:
            num = num+len(left)-i
            result.append(right[j])
            j+=1
        else:
            result.append(left[i])
            i+=1
    result+=left[i:]
    result+=right[j:]
    return result,num

print(inversion(num_lst))
    

