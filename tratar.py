# f = open("resultado.txt",'r')
# texto = f.readlines()
# print(texto)

# f = open("resultado.txt",'r')
# texto = f.readlines()
# print (f)
# print(60 * '#')
# x = 0

# while x < len(texto):
#     if texto[x] == "\n":
#         local = texto.index(texto[x])
#         texto.pop(local)
#     else:
#         texto[x] = texto[x].split(',')
#         x += 1

# # Esse for abaixo aqui é só para tirar o "\n" em algumas strings, é opcional.

# # for i in texto:
# #     local = texto.index(i) # Local do i em texto
# #     for b in i:
# #         local2 = texto[local].index(b) # Local2 do b em i ( local )
# #         if "\n" in b:
# #             texto[local][local2] = b.replace("\n",'') # Substitui o valor de acordo com "local" e "local2"

# lista = texto
# print("lista =",lista)


# from posixpath import split


# with open("Resultado.txt", "r") as arquivo:
#     texto = arquivo.readlines()
#     print(texto)
# with open("Resultado.txt", "a") as arquivo:
#     arquivo.write("%s\n" % texto)
#     print(arquivo) 
# arquivo.close()       

""" arquivo = open("Resultados.txt","r")
linha = arquivo.readline()
lista = []
while linha:
    valores = linha.split()
    lista.append(valores)
    linha = arquivo.readline()
for i in lista:
    arquivo2 = open("Resultados.txt", "w")
    arquivo2.write("%s\n" % lista)
    arquivo.close()
    

print(lista) """


""" def substituir_espacos_por_virgulas(arquivo):
    # Abrir e ler o arquivo
    with open(arquivo, 'r') as f:
        conteudo = f.read()
        print(conteudo)

    # Modificar o conteúdo
    conteudo_modificado = conteudo.replace(" ", ",")
    print(conteudo_modificado)

    # Salvar as modificações
    with open(arquivo, 'w') as f:
        f.write(conteudo_modificado)

# Uso
arquivo = 'resultados_novos.txt'
substituir_espacos_por_virgulas(arquivo) """

""" import re

def substituir_espacos_por_virgulas(arquivo):
    # Abrir e ler o arquivo
    with open(arquivo, 'r') as f:
        conteudo = f.read()
        print(conteudo)

    # Modificar o conteúdo usando regex para substituir sequências de espaços ou tabulações por vírgulas
    conteudo_modificado = re.sub(r'  +', ',', conteudo)
    print(conteudo_modificado)

    # Salvar as modificações
    with open(arquivo, 'w') as f:
        f.write(conteudo_modificado)

# Uso
arquivo = 'resultados_novos.txt'
substituir_espacos_por_virgulas(arquivo)

 """

def substituir_tabs_por_virgulas(arquivo):
    # Ler o arquivo linha por linha e substituir as tabulações
    with open(arquivo, 'r') as f:
        linhas = [linha.replace("\t", ",") for linha in f.readlines()]

    # Salvar as modificações
    with open(arquivo, 'w') as f:
        f.write(''.join(linhas))

# Uso
nome_do_arquivo = 'resultados_novos.txt'
substituir_tabs_por_virgulas(nome_do_arquivo)

