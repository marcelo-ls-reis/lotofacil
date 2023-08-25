import random

def sortear_numeros():
    return sorted(random.sample(range(1, 26), 15))

def tem_mais_de_7_consecutivos(sequencia):
    cont_consecutivos = 1
    for i in range(1, len(sequencia)):
        if sequencia[i] == sequencia[i-1] + 1:
            cont_consecutivos += 1
            if cont_consecutivos > 7:
                return True
        else:
            cont_consecutivos = 1
    return False

def ler_sequencias_do_arquivo(resultados):
    sequencias = []
    try:
        with open(resultados, 'r') as arquivo:
            print(resultados)
            for linha in arquivo:
                sequencias.append(list(map(int, linha.strip().split(','))))
                print(sequencias[-1])
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        pass
    return sequencias

def salvar_sequencia_no_arquivo(jogos, sequencia):
    with open(jogos, 'a') as arquivo:
        arquivo.write(','.join(map(str, sequencia)) + '\n') # Transforma a lista em uma string separada por vírgulas.

def main():
    resultados = "resultadoso.txt"
    jogos = "jogos.txt"
    sequencias_sorteadas = ler_sequencias_do_arquivo(resultados)
    
    quantidade_sorteados = int(input("Quantos sorteios você quer realizar? "))

    for _ in range(quantidade_sorteados):
        sequencia_atual = sortear_numeros()

        # Verifica se a sequência já foi sorteada e se possui mais de 7 números consecutivos.
        while sequencia_atual in sequencias_sorteadas or tem_mais_de_7_consecutivos(sequencia_atual):
            sequencia_atual = sortear_numeros()
        
        sequencias_sorteadas.append(sequencia_atual)
        salvar_sequencia_no_arquivo(jogos, sequencia_atual)
        print(f"Sequência sorteada: {sequencia_atual}")

if __name__ == "__main__":
    main()
