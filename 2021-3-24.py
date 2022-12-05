import gen_num  
num_lst = gen_num.gen_num2(30)
print(num_lst)

def count_sort(A):
    min_num = min(A) 
    max_num = max(A) 
    delta = max_num-min_num
    count = [0 for i in range(min_num,max_num+1)]
    for item in A:
        count[item-min_num] +=1
    print(count)
    result = []
    for i in range(len(count)):
        while count[i]>0:
            result.append(i+min_num)
            count[i] -=1
    return result

print(count_sort(num_lst))
    



