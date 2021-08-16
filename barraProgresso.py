from tkinter import *
from tkinter import ttk
import time
import os


def alterarValor(m):
    cont=0
    etapas=m
    while cont<etapas:
        cont+=1
        time.sleep(0.5)
        valor.set(cont)
        app.update()
    
    
app = Tk()
app.title('')

app.geometry('300x500')
app.configure(background='#404040')

#Dimensoes da janela 
largura = 300
altura = 500

#Resolução da tela
largura_tela = app.winfo_screenwidth()
altura_tela = app.winfo_screenheight()

#posição na janela
posx = largura_tela/2 - largura/2
posy = altura_tela/2 - altura/2

#Definir a centralização da janela no monitor
app.geometry('%dx%d+%d+%d'% (largura,altura,posx,posy))

lbl = Label(app,text='Barra de progresso',bg='#404040',fg='#fff',font='Times 20 bold italic')
lbl.place(x=10,y=10, width=280, height=30)

valor = DoubleVar()
valor.set(0)

barra=ttk.Progressbar(app,variable=valor,maximum=100)
barra.place(x=10,y=50, width=280,height=30)

botao = Button(app,text="Iniciar",command=lambda:alterarValor(100))
botao.place(x=10,y=90,width=280,height=30)


app.mainloop()