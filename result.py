from tkinter import *
from sys import argv

resultado = argv


tela = Tk()
tela.title("Jogo da velha")
tela.geometry("300x150")
tela.resizable(False, False)

try:
    Label (tela, text = f"\n\n{resultado[1]}", font = "bold 15").pack(side = TOP)
except:
    Label (tela, text = "\n\nNenhum vencedor encontrado", font = "bold 15").pack(side = TOP)

tela.mainloop()