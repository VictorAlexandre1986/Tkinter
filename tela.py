from tkinter import *

janela = Tk()
janela.title('Primeiro App')
#Os dois primeiros argumentos definem a dimensão os 2 ultimos a posição x e y
janela.geometry('600x500+50+50')
#resizable permiti redimensionar a janela com o mouse
janela.resizable(True,True)#Um true é da largura o outro é da altura

#Tamanho minimo no redimensionamento
janela.minsize(width=400, height=300)
#Tamanho maximo no redimensionamento
janela.maxsize(width=800, height=600)

janela.mainloop()