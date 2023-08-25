import random

def sortear_numeros():
    return sorted(random.sample(range(1, 26), 15))

def ler_sequencias_do_arquivo(resultados):
    sequencias = []
    try:
        with open(resultados, 'r') as arquivo:
            for linha in arquivo:
                sequencias.append(list(map(int, linha.strip().split(','))))
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        pass  # Se o arquivo não existir, não faz nada e retorna uma lista vazia.
    return sequencias

def salvar_sequencia_no_arquivo(resultados, sequencia):
    with open(resultados, 'a') as arquivo:
        arquivo.write(','.join(map(str, sequencia)) + '\n')

def main():
    resultados = "sequencias_sorteadas.txt"
    sequencias_sorteadas = ler_sequencias_do_arquivo(resultados)
    
    quantidade_sorteados = int(input("Quantos sorteios você quer realizar? "))

    for _ in range(quantidade_sorteados):
        sequencia_atual = sortear_numeros()
        
        # Verifica se a sequência já foi sorteada.
        while sequencia_atual in sequencias_sorteadas:
            sequencia_atual = sortear_numeros()
        
        sequencias_sorteadas.append(sequencia_atual)
        salvar_sequencia_no_arquivo(resultados, sequencia_atual)
        print(f"Sequência sorteada: {sequencia_atual}")

if __name__ == "__main__":
    main()
