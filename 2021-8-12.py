import gen_num
num_lst =  gen_num.gen_num1(100)

def tim_sort(lst):
    length = len(lst)
    runs= []
    new_run = [lst[0]]
    sorted_array = []
    for i in range(1,length-1):
        if lst[i]<lst[i+1]:
            runs.append(new_run)
            new_run = [lst[i]]
        else:
            new_run.append(lst[i])
    runs.append(new_run)

    for run in runs:
        sorted_array = merge(sorted_array,run)
    return sorted_array

def merge(left,right):
    i,j = 0,0
    result = []
    while i<len(left)and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result+=left[i:]
    result+=right[j:]
    return result

print(tim_sort(num_lst))
