# resultado = [1, 2, 3, 6, 8, 10, 13, 14, 15, 16, 18, 19, 21, 24, 25]
# resultado = [1, 2, 4, 5, 6, 9, 10, 13, 16, 17, 18, 19, 22, 24, 25]
resultado = [1, 2, 3, 6, 8, 10, 13, 14, 15, 16, 18, 19, 21, 24, 25]
            

sequencia = []
contador = 0
for i in resultado:
    contador += 1
    if contador == 1:
        sequencia.append(i)
    else:
        if i == sequencia[-1] + 1: # Se o numero for igual ao anterior + 1
            sequencia.append(i)
        else:
            print(sequencia)
            sequencia = []
            sequencia.append(i)
