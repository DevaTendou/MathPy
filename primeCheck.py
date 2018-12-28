global exp

def primeCheck(prime):
    global exp
    exp <<= 1
    if not ((exp) % prime) - 1:
        print(prime)
    
exp = 1
for i in range(3, 0xFFFFFFFFFFFFFFFFFFFFFF, 2):
    number = primeCheck(i)
    if number:
        print(number)



        
    
