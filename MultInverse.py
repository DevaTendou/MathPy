#Multiplicative Inverse
def isCoprime(a, m):
    while m:
        a, m = m, a % m
    if a == 1:
        return True
    else:
        return False

def invMult(a, totient, m):
    return pow(a, totient - 1, m)

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def listPrimes(n):
    ls = [2]
    for i in range(1, n + 1, 2): 
        if pow(2, i - 1, i) == 1:
            ls.append(i)
    return ls

def phi(num):
    result = num
    p = 2
    while p*p <= num:
        if num % p == 0:
            while num % p == 0:
                num /= p
            result *= (1.0 - (1.0 / p))
        p += 1
    if num > 1:
        result *= (1 - (1 / num))
    return int(result)

'''def test(num):
    pfs = listPrimes(1000)
    index = 0
    for pfi in pfs:
        i = num/pfi
        if i == num//pfi:
            num = i
            index += 1
    return index'''


        
    


'''p = 18593917
q = 11110487
m = p * q
e = 68862481134395
print(m)

totient = (p - 1) * (q - 1)
print(totient)

d = pow(e, phi(totient) - 1, totient)
print(d)

test = (5*24556884961225) % 80031270838596
print(test)'''

print(phi(80031270838596))




