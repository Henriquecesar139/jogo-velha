from tkinter import *
from os import system

def acao(bt, f, c):
    global cont
    #A jogada só pode ser feita se o botão estiver vazio
    if bt['text'] == '':
        cont = cont + 1
        #contador recebe +1
        #contador par: vez de O
        #contador ímpar: vez de X
        if cont % 2 == 0:
            texto["text"] = 'O'
            bt['text'] = 'X'
            posicoes[f][c] = 'X'

        else:
            texto["text"] = 'X'
            bt['text'] = 'O'
            posicoes[f][c] = 'O'

        #verificação horizontal
        if ['X', 'X', 'X'] in posicoes:
            resultado('X')
        elif ['O', 'O', 'O'] in posicoes:
            resultado('O')

        #verificação vertical
        for c in range(3):
            if posicoes[0][c] + posicoes[1][c] + posicoes[2][c] == 'XXX':
                resultado('X')
            elif posicoes[0][c] + posicoes[1][c] + posicoes[2][c] == 'OOO':
                resultado('O')

        #verificação diagonal
        if posicoes[0][0] + posicoes[1][1] + posicoes[2][2] == 'XXX':
            resultado('X')
        elif posicoes[0][0] + posicoes[1][1] + posicoes[2][2] == 'OOO':
            resultado('O')
        elif posicoes[0][2] + posicoes[1][1] + posicoes[2][0] == 'XXX':
            resultado('X')
        elif posicoes[0][2] + posicoes[1][1] + posicoes[2][0] == 'OOO':
            resultado('O')

        #verificação de empate (se não houver botões vazios nem vitórias)
        i = 0
        for c in botoes:
            if c['text'] != '':
                i += 1
                if i == 9:
                    resultado('E')

    else:
        pass

#função que exibe o resultado
def resultado(v):
    if v == 'X':
        system('python3 result.py VENCEDOR:X')
    elif v == 'O':
        system('python3 result.py VENCEDOR:O')
    elif v == 'E':
        system('python3 result.py EMPATE')
    #ao exibir resultado, abre uma nova janela e destroi a atual
    tela.destroy()
    system('python3 velha.py')

#lista com as posições
posicoes = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]


#tela
tela = Tk()
tela.title("Jogo da velha")
tela.geometry("400x500")
tela.resizable(False, False)

#contador que define a vez de X e O
cont = 1

texto = Label (tela, text = 'X', font = "bold 20")
texto.pack(side = TOP)

#cada botão passa como parâmetro, ele mesmo (para mudar o texto), dois números referentes a fileira e coluna

b1 = Button (tela, width = 5, height = 2, command = lambda : acao(b1, 0, 0))
b1.place(x = 50, y = 100)

b2 = Button (tela, width = 5, height = 2, command = lambda : acao(b2, 0, 1))
b2.place(x = 165, y = 100)

b3 = Button (tela, width = 5, height = 2, command = lambda : acao(b3, 0, 2))
b3.place(x = 280, y = 100)

b4 = Button (tela, width = 5, height = 2, command = lambda : acao(b4, 1, 0))
b4.place(x = 50, y = 200)

b5 = Button (tela, width = 5, height = 2, command = lambda : acao(b5, 1, 1))
b5.place(x = 165, y = 200)

b6 = Button (tela, width = 5, height = 2, command = lambda : acao(b6, 1, 2))
b6.place(x = 280, y = 200)

b7 = Button (tela, width = 5, height = 2, command = lambda : acao(b7, 2, 0))
b7.place(x = 50, y = 300)

b8 = Button (tela, width = 5, height = 2, command = lambda : acao(b8, 2, 1))
b8.place(x = 165, y = 300)

b9 = Button (tela, width = 5, height = 2, command = lambda : acao(b9, 2, 2))
b9.place(x = 280, y = 300)

botoes = [b1, b2, b3, b4, b5, b6, b7, b8, b9]

tela.mainloop()