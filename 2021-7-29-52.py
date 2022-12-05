
'''
backpack 
A B C 
4 3 5
5000 200 10
s<=9
'''
MAX = 9
def packet(w,p):
    '''
    w:weight seq
    p:price seq
    '''
    global MAX
    p_w_dict = dict(zip(p,w))
    sorted(p_w_dict)
    print(p_w_dict)
    p_sorted =p
    print(list(p_sorted))
    result = []
    left = MAX
    for item in p_sorted:
        print(item)
        if left>0:
            a = min(p_w_dict[item],left)
            print(a)
            result.append(a)
            left  = left - p_w_dict[item]
    return result


w = [4,3,5]
p = [5000,200,10]
print(packet(w,p))

