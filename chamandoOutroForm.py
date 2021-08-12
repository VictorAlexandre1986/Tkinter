from tkinter import *
import os

pastaApp = os.path.dirname(__file__)

def imprimir():
    pass

def novoContato():
    exec(open(pastaApp+'\\NovoContato.py').read(),{'x':10})

app=Tk()
app.title('Menu')
app.geometry('500x300')
app.configure(background='#404040')

barra = Menu(app)
menuContatos=Menu(barra,tearoff=0)
menuContatos.add_command(label='Novo', command=novoContato)
menuContatos.add_command(label='Pesquisar', command=imprimir)
menuContatos.add_command(label='Deletar', command=imprimir)
menuContatos.add_separator()
menuContatos.add_command(label='Fechar', command=app.quit)
barra.add_cascade(label='contatos',menu=menuContatos)



app.config(menu=barra)
app.mainloop()