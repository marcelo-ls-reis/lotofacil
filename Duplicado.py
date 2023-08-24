
# crie uma lista de numeros inteiros
# as listas tem o tamnho de 10 elementos 
# as listas internas tem numeros de a 1 a 10 e podem ser duplicados

lista = [
    [1,2,3,4,5,6,7,8,9,10],
    [9,1,8,9,9,7,2,1,6,8],
    [1,3,2,8,9,5,4,7,6,9],
    [3,8,2,8,6,7,7,3,1,9],
]

# crie uma funçaõ que recebe uma lista de listas e ache o primeiro elemento duplicado
# se não existir duplicado, retorne -1
def duplicado(lista):
    for i in lista:
        for j in i:
            if i.count(j) > 1:
                return j
                print(j)
    return -1

duplicado(lista)
    