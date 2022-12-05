import gen_num  

num_lst = gen_num.gen_num1(20)
print(num_lst)

def mergeSort(A):

    '''
    Args:
    A:num_list
    分
    '''
    if len(A)<=1:
        return A
    mid = int((len(A)/2))
    print('mid:',mid) # 1 1 2 5 10 
    left = mergeSort(A[:mid])#[0,mid-1]
    right = mergeSort(A[mid:])#[mid,len(A)-1]
    return merge(left,right)

def merge(left,right):
    #合
    i,j=0,0
    result = []
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
   # left[i:],right[j:] 总有一个是空的
    result +=left[i:] #将left剩下的放进去
    result +=right[j:] #将right剩下的放进去
    print(result)
    return result

B = mergeSort(num_lst)
print(B)

