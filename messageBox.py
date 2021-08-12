from tkinter import *
from tkinter import messagebox
import os

def caixa1():
    messagebox.showinfo(title='Caixa simples',message='Message box simples')
    
def caixa2():
    messagebox.showwarning(title='Caixa warning',message='Message box warning')
    
def caixa3():
    messagebox.showerror(title='Caixa warning',message='Message box warning')
    
app = Tk()
app.title('')

app.geometry('300x500')
app.configure(background='#404040')


#anchor N=norte S=sul E=leste W=oeste, posiciona o texto dentro do seu container
#Por Exemplo : anchor=E
lbl = Label(app,text='Caixas de mensagens',bg='#404040',fg='#fff',font='Times 20 bold italic')
lbl.place(x=10,y=10, width=280, height=30)


btn1 = Button(app,text='Selecionar',command=caixa1)
btn1.place(x=10,y=50,width=280,height=30)

btn2 = Button(app,text='Selecionar',command=caixa2)
btn2.place(x=10,y=90,width=280,height=30)

btn3 = Button(app,text='Selecionar',command=caixa3)
btn3.place(x=10,y=130,width=280,height=30)

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



    
    
app.mainloop()