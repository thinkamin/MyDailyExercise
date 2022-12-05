
def lcm(a,b):
    return a*b/(gcd(a,b))


def gcd(a,b):
    if b!=0:
        return gcd(b,a%b)
    else:
        return a


nums = input('2个整数，并以，分割\n')
# print(nums)
nums = nums.split(',')
nums = [int(num) for num in nums]
print(lcm(nums[0],nums[1]))




