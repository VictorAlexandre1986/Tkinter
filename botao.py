from tkinter import *

def msg(params):
    print(f'Bom dia, {params}')
    
def msg2():
    print(f'Bom dia')

    
janela = Tk()
janela.title('Primeiro App')

janela.geometry('600x500+50+50')

btn = Button(janela, text='Executar',command=lambda:msg('Victor'))
btn.pack()

btn2 = Button(janela, text='Executar',command=msg2)
btn2.pack()

janela.mainloop()

