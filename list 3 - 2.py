import math
import random

def is_prime(num, test_count):
    for i in range(test_count):
        rnd = random.randint(1, num - 1)
        if (rnd ** (num - 1) % num != 1):
            return False
    return True
def NWK(a,b):
    if b==0:
        return a
    else:
        return NWK(b, a%b)
def trzy7(iter):
    for j in range(len(str(iter))-2):
        if str(i)[j:j+7]==7*'7':
            return 1
    return 0
od=int('1'+9*'0')
do=int(10*'9')
for i in range(od,do+1):
    if trzy7(i) and liczp(i):
         print(i)          
