#Montgomery Modular Multiplication
a = 43
b = 56
N = 97

def findR_Exp(mod):
    exp = 0
    while (1 << exp) < mod:
        exp += 1
    return exp

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def multInverse(number, mod):
    temp = number
    while True:
        if number % mod == 1:
            return number // temp
        number += temp

expR = findR_Exp(N)
R = 1 << expR
invR = multInverse(R, N)
K = ((invR << expR) - 1) >> expR
#aPrime = (a << expR) % N
#bPrime = (b << expR) % N
cPrime = ((a*b) << (expR)) % N #
s = (cPrime*K) >> expR
t = cPrime + (s*N)
u = t >> expR
if u > N:   u -= N
c = (cPrime * invR) % N
print(c)
