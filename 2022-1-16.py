from my import gen_num

num_lst = gen_num()

def insert_sort(A):
    length = len(A)
    for i in range(1,length):#1,n-1
        key = A[i]
        j = i
        while j>0 and A[j-1]>key:
            A[j]=A[j-1]
            j-=1
        A[j]=key
    return A
# print(insert_sort(num_lst))
def shell_sort(A):
    gaps = [8,4,2,1]
    length = len(A)
    for gap in gaps:
        if length>gap:
            for i in range(gap+1,length):#gap+1,n-1
                key = A[i]
                j=i
                while A[j-gap]>key and j-gap>=0:
                    A[j]=A[j-gap]
                    j-=gap
                A[j]=key
    return A
# print(shell_sort(num_lst))
import heapq
heapq.heapify(num_lst)
result = []
for i in range(len(num_lst)):#0,n-1
    result.append(heapq.heappop(num_lst))
print(result)

