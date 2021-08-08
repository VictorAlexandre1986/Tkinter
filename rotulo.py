from tkinter import *

janela = Tk()
janela.title('Dimensao')


label = Label(janela, text='Nome : ', bg='#404040', fg='#fff',font='Times 20 bold italic')
label.pack()

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