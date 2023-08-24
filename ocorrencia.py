from cProfile import label  # Importa o módulo label do pacote cProfile
from os import os
from struct import pack
from tkinter import Label, Tk

os.system("cls")
from jogos import jogos  # Importa a lista de jogos

contador15 = 0
contador14 = 0
contador13 = 0
contador12 = 0
contador11 = 0
contador10 = 0
contador = 0
d = ['1','3','6','8','11','12','14','15','17','18','19','20','21','23','25']



for i in jogos:
    contador += 1
    x = set(i) & set(d)  # Verifica se o numero da carteira esta no dicionario
    # print("Acertou: ", len(x), "=", x)
    if len(x) == 15:
        contador15 += 1
    if len(x) == 14:
        contador14 += 1
    if len(x) == 13:
        contador13 += 1
    if len(x) == 12:
        contador12 += 1  
    if len(x) == 11:
        contador11 += 1 
    if len(x) == 10:
        contador10 += 1

raiz = Tk()              # Cria a janela
w = Label(raiz, text="\n15 pontos = " + str(contador15) + "\n\n14 pontos = " + str(contador14) + "\n\n13 pontos = " + str(contador13) + "\n\n12 pontos = " + str(contador12) + "\n\n11 pontos = " + str(contador11) + "\n\nApostas = " + str(contador)) # Cria um label
w.pack()                  # Coloca o widget na janela      
raiz.mainloop()           # Inicia o loop da janela
print(f'Cartões com 15 pontos: {contador15}')
print(f'Cartões com 14 pontos: {contador14}')
print(f'Cartões com 13 pontos: {contador13}')
print(f'Cartões com 12 pontos: {contador12}')
print(f'Cartões com 11 pontos: {contador11}')
print(f'Cartões com 10 pontos: {contador10}')
print(f'Número de apostas: {contador}')