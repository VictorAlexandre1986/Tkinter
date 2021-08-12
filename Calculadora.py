from tkinter import *

app = Tk()
app.title('')

app.geometry('300x500')
app.configure(background='#404040')


#anchor N=norte S=sul E=leste W=oeste, posiciona o texto dentro do seu container
#Por Exemplo : anchor=E
lbl = Label(app,text='Calculadora',bg='#404040',fg='#fff',font='Times 20 bold italic')
lbl.place(x=10,y=10, width=280, height=30)

txb = Entry(app)
txb.place(x=10,y=60,width=280,height=30 )

btn = Button(app, text='0' , command=display(0))
btn.place(x=10, y=100, width=60, height=60)

btn1 = Button(app, text='1' , command='')
btn1.place(x=80, y=100, width=60, height=60)

btn2 = Button(app, text='2' , command='')
btn2.place(x=150, y=100, width=60, height=60)

btn3 = Button(app, text='C' , command='')
btn3.place(x=220, y=100, width=60, height=60)

btn4 = Button(app, text='3' , command='')
btn4.place(x=10, y=170, width=60, height=60)

btn5 = Button(app, text='4' , command='')
btn5.place(x=80, y=170, width=60, height=60)

btn6 = Button(app, text='5' , command='')
btn6.place(x=150, y=170, width=60, height=60)

btn7 = Button(app, text='+' , command='')
btn7.place(x=220, y=170, width=60, height=60)

btn8 = Button(app, text='6' , command='')
btn8.place(x=10, y=240, width=60, height=60)

btn9 = Button(app, text='7' , command='')
btn9.place(x=80, y=240, width=60, height=60)

btn10 = Button(app, text='8' , command='')
btn10.place(x=150, y=240, width=60, height=60)

btn11 = Button(app, text='-' , command='')
btn11.place(x=220, y=240, width=60, height=60)

btn12 = Button(app, text='9' , command='')
btn12.place(x=10, y=310, width=60, height=60)

btn9 = Button(app, text='.' , command='')
btn9.place(x=80, y=310, width=60, height=60)

btn10 = Button(app, text='M+' , command='')
btn10.place(x=150, y=310, width=60, height=60)

btn11 = Button(app, text='/' , command='')
btn11.place(x=220, y=310, width=60, height=60)

btn12 = Button(app, text='=' , command='')
btn12.place(x=10, y=380, width=200, height=60)

btn13 = Button(app, text='*' , command='')
btn13.place(x=220, y=380, width=60, height=60)

#Dimensoes da janela 
largura = 300
altura = 500

#Resolução da tela
largura_tela = app.winfo_screenwidth()
altura_tela = app.winfo_screenheight()

#posição na janela
posx = largura_tela/2 - largura/2
posy = altura_tela/2 - altura/2

def display(valor):
    pass


#Definir a centralização da janela no monitor
app.geometry('%dx%d+%d+%d'% (largura,altura,posx,posy))
app.mainloop()