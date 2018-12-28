import math as m

mensagem = "Hello There!"
encoding = 8

number = 0
while mensagem:
	number <<= encoding
	number |= ord(mensagem[0]) 
	mensagem = mensagem[1:]

lenMensagem = len(bin(number)) - 2



def findDivs(number):
	start, divs, exclude = 2, [], []
	
	if pow(2, number - 1, number) == 1: return number
	
	while number != 1:
		if not (number % start): 
			divs.append(start)
			number //= start
		else: start += 1
	return divs
	
print(findDivs(67_280_421_310_721))

