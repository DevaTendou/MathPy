import random as ran

def binGCD(x, y):
    g = 1
    while (x & 1) == 0 and (y & 1) == 0:
        x >>= 1
        y >>= 1
        g <<= 1
    while x:
        if   (x & 1) == 0: x >>= 1
        elif (y & 1) == 0: y >>= 1
        else:
            t = abs(x-y) >> 1
            if x < y:   y = t
            else: x = t
    return y*g

'''def subquadraticGCD(x, y):
    s = '''

def xorGCD(x, y):
    while y:
        x %= y
        y ^= x
        x ^= y
        y ^= x
    return x

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

