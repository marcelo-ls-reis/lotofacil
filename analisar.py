# Cria um dicionário para contar a frequência de cada número
frequencia = {i: 0 for i in range(1, 26)}  # A Lotofácil tem números de 1 a 25

# Abre o arquivo para leitura
with open('sorteadas.txt', 'r') as arquivo:
    for linha in arquivo:
        # Transforma a linha em uma lista de números
        numeros = list(list(map(int, linha.strip().split(','))))

        # Atualiza a frequência de cada número
        for num in numeros:
            if 1 <= num <= 25:  # Certifica-se de que o número é válido
                frequencia[num] += 1

# Imprime os números e suas respectivas frequências, em ordem decrescente
for numero, freq in sorted(frequencia.items(), key=lambda x: x[1], reverse=True):
    print(f'Número {numero}: {freq} vezes')

