from tkinter import *
#from tkinter import ttk
import os

def imprimir():
    esp=str(lb.get(ACTIVE))
    print(esp)
    
def adicionar():
    esp=str(entrada.get())
    lb.insert(END,esp)
    
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

lbl = Label(app,text='ListBox',bg='#404040',fg='#fff',font='Times 20 bold italic')
lbl.place(x=10,y=10, width=280, height=30)

esportes = ['Futebol','Volei','Basquete']

lb=Listbox(app)
for esporte in esportes:
    lb.insert(END,esporte) 
     
lb.place(x=10,y=50, width=280,height=100)

entrada = Entry(app)
entrada.place(x=10,y=160,width=280,height=30)


botao = Button(app,text="Imprimir", command=imprimir)
botao.place(x=10,y=200,width=280,height=30)

botao = Button(app,text="Inserir", command=adicionar)
botao.place(x=10,y=240,width=280,height=30)


app.mainloop()