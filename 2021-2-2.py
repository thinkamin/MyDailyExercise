#insert sort
import random

num_list = list(range(10))#[0,9]
random.shuffle(num_list)
# print(num_list)

def insertSort(A,pos,value):
    '''
    Arguments:
    A:num_list
    pos:value index [1,length-1]
    value:value
    '''
    i = pos -1
    while i>=0 and A[i]>value:
        A[i+1]=A[i]
        i=i-1
    A[i+1]=value

g = len(num_list)
for i in range(1,b):#[1,9]
    insertSort(num_list,i,num_list[i])
print(num_list)




