#Euclidian Coords

def matrixDim(n):
    lista = []
    for x in range(1, n+1):
        for y in range(1, n+1):
            coord = []
            coord.append(x)
            coord.append(y)
            lista.append(coord)
    return lista

def distance(element1, element2):
    if element1[-1] == element2[-1] and element1[0] == element2[0]:
        return 0
    elif element1[-1] == element2[-1]:
        return ((element2[0] - element1[0])**2)**0.5
    elif element1[0] == element2[0]:
        return ((element2[-1] - element1[-1])**2)**0.5
    else:
        return (((element2[0] - element1[0])**2) + (element2[-1] - element1[-1])**2)**0.5

lista = matrixDim(3)

dList = []
for element1 in lista:
    for element2 in lista:
        print(element1, element2, " -> ", distance(element1, element2), "\n")
