from tkinter import *
import os

def imprimir():
    with open('arquivo.txt','w') as file:
        file.write(txarea.get('1.0',END))
        file.write(txb.get())
    print(txarea.get('1.0',END))
    print(txb.get())
    
    
app = Tk()
app.title('')

app.geometry('300x500')
app.configure(background='#404040')


#anchor N=norte S=sul E=leste W=oeste, posiciona o texto dentro do seu container
#Por Exemplo : anchor=E
lbl = Label(app,text='Editor de texto',bg='#404040',fg='#fff',font='Times 20 bold italic')
lbl.place(x=10,y=10, width=280, height=30)

txarea = Text(app)
txarea.place(x=10,y=60,width=280,height=300 )

txb = Entry(app)
txb.place(x=10,y=370,width=280,height=30 )

btn = Button(app, text='Imprimir & Salvar' , command=imprimir)
btn.place(x=10, y=410, width=280, height=60)



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