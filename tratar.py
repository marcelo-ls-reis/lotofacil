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

arquivo = open("Resultados.txt","r")
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
    

print(lista)
