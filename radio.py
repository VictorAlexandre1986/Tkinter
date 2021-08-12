from tkinter import *
import os

def imprimir():
    ve=valor.get()
    print(ve)
    
app = Tk()
app.title('')

app.geometry('300x500')
app.configure(background='#404040')

listaEsportes=['Futebol','Volei','Basquete']
valor = StringVar()
valor.set(listaEsportes[0])

#anchor N=norte S=sul E=leste W=oeste, posiciona o texto dentro do seu container
#Por Exemplo : anchor=E
lbl = Label(app,text='Esportes',bg='#404040',fg='#fff',font='Times 20 bold italic')
lbl.place(x=10,y=10, width=280, height=30)

op_esportes = OptionMenu(app,valor,*listaEsportes)
op_esportes.place(x=10,y=60,width=100,height=30 )



btn_esporte = Button(app,text='Selecionar',command=imprimir)
btn_esporte.place(x=10,y=180,width=290,height=30)



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