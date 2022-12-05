def gcd(a,b):
    if b!=0:
        return gcd(b,a%b)
    else:
        return a

import random
for i in range(100):
    a = random.randint(1,100)
    b = random.randint(1,100)
    print(a,b,gcd(a,b))
