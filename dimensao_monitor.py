from tkinter import *

janela = Tk()
janela.title('Dimensao')

largura = 600
altura = 300

#Resolução da tela
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

#posição na janela
posx = largura_tela/2 - largura/2
posy = altura_tela/2 - altura/2

#Definir a centralização da janela no monitor
janela.geometry('%dx%d+%d+%d'% (largura,altura,posx,posy))

print(largura_tela,altura_tela)

janela.mainloop()
