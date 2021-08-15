from tkinter import *
import os

def imprimir():
    senha=vsenha.get()
    print(senha)
    
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

lbl = Label(app,text='Senha',bg='#404040',fg='#fff',font='Times 20 bold italic')
lbl.place(x=10,y=10, width=280, height=30)

vsenha=StringVar()

input = Entry(app, textvariable=vsenha,show="*")
input.place(x=10,y=50 , width=280, height=30)

botao = Button(app,text="Imprimir Senha", command=imprimir)
botao.place(x=10,y=90,width=280,height=30)


    
    
app.mainloop()