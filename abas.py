from tkinter import *
from tkinter import ttk
import os

def imprimir():
    valor=str(sb_valores.get())
    print(valor)
    
    
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

nb=ttk.Notebook(app)
nb.place(x=0,y=40,width=300,height=460)

lbl = Label(app,text='Abas',bg='#404040',fg='#fff',font='Times 20 bold italic')
lbl.place(x=10,y=10, width=280, height=30)

aba1=Frame(nb)
aba2=Frame(nb)

nb.add(aba1,text='Aba1')
nb.add(aba2,text='Aba2')

lbl1=Label(aba1,text="Curso de Python")
lbl1.place(x=100,y=50,width=100,height=30)

lbl1=Label(aba2,text="Curso de Tkinter")
lbl1.place(x=100,y=50,width=100,height=30)

app.mainloop()