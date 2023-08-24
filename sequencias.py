class Sequencia:
    def __init__(self, lista):
        self.lista = lista
    
    def maior_sequencia(self):
        # Inicializa a variável de contagem da sequência atual e da sequência máxima
        seq_atual = seq_max = 1
        
        # Itera sobre a lista, verificando se cada elemento é igual ao seu sucessor
        for i in range(len(self.lista)-1):
            if self.lista[i] + 1  == self.lista[i+1]: 
               # Se os elementos são iguais, incrementa a sequência atual
                seq_atual += 1
            else:
                # Se os elementos são diferentes, verifica se a sequência atual é maior
                # que a sequência máxima, e atualiza a sequência máxima se for o caso
                if seq_atual > seq_max:
                    seq_max = seq_atual
                seq_atual = 1
        
        # Retorna a sequência máxima encontrada
        return seq_max


# Exemplo de uso
lista = [1,3,5,7,8,9,10,12,13,14,16,17,19,21,25]
seq = Sequencia(lista)
print(seq.maior_sequencia())  # Saída: 3 (a maior sequência é [5, 5, 5])


