def encontrar_subsequentes(numeros):
    """Identifica conjuntos de números em sequência em uma lista."""
    subsequentes = []
    atual = [numeros[0]]

    for i in range(1, len(numeros)):
        if numeros[i] == atual[-1] + 1:
            atual.append(numeros[i])
        else:
            if len(atual) > 1:
                subsequentes.append(tuple(atual))
            atual = [numeros[i]]
    if len(atual) > 1:
        subsequentes.append(tuple(atual))

    return subsequentes

# Dicionário para contar a frequência de cada subsequência
frequencia_subseq = {}

# Abre o arquivo para leitura
with open('resultadoso.txt', 'r') as arquivo:
    for linha in arquivo:
        # Transforma a linha em uma lista de números
        numeros = sorted(list(map(int, linha.strip().split(','))))

        # Encontra as subsequências na linha atual
        for subseq in encontrar_subsequentes(numeros):
            if subseq in frequencia_subseq:
                frequencia_subseq[subseq] += 1
            else:
                frequencia_subseq[subseq] = 1

# Imprime as subsequências e suas respectivas frequências, em ordem decrescente
for subseq, freq in sorted(frequencia_subseq.items(), key=lambda x: x[1], reverse=True):
    print(f'Subsequência {subseq}: {freq} vezes')

