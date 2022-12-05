#merge sort
import random

# 原理见
def gen_A():
    num_list = list(range(10))#[0,9]
    random.shuffle(num_list)
    return  num_list
# print(num_list)

def mergeSort(A):

    '''
    Args:
    A:num_list
    分
    '''
    if len(A)<=1:
        return A
    mid = int((len(A)/2))
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
    result +=left[i:] #将left剩下的放进去
    result +=right[j:] #将right剩下的放进去
    return result

if __name__=='__main__':
    A = gen_A()
    B = mergeSort(A)
    print(B)

