from resultadoso import lista


class Sequencia:
    def __init__(self, lista):
        self.lista = lista
    
    def maiorSequencia(self, lista):
        """
        Método que encontra a maior sequência de números em uma lista com listas de 15 elementos.

        :param lista: lista contendo listas de 15 elementos.
        :return: maior sequência encontrada.
        """

        maior_seq = []
        for i in range(len(lista)):
            seq_atual = []
            for j in range(len(lista[i])):
                if not seq_atual:
                    seq_atual.append(lista[i][j])
                elif lista[i][j] == seq_atual[-1] + 1:
                    seq_atual.append(lista[i][j])
                else:
                    if len(seq_atual) > len(maior_seq):
                        maior_seq = seq_atual
                    seq_atual = [lista[i][j]]
            if len(seq_atual) > len(maior_seq):
                maior_seq = seq_atual
        
        return maior_seq

seq = Sequencia(lista)

print(seq.maiorSequencia(lista))