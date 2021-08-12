from tkinter import *

def imprimir():
    pass

app=Tk()
app.title('Menu')
app.geometry('500x300')
app.configure(background='#404040')

barra = Menu(app)
menuContatos=Menu(barra,tearoff=0)
menuContatos.add_command(label='Novo', command=imprimir)
menuContatos.add_command(label='Pesquisar', command=imprimir)
menuContatos.add_command(label='Deletar', command=imprimir)
menuContatos.add_separator()
menuContatos.add_command(label='Fechar', command=app.quit)
barra.add_cascade(label='contatos',menu=menuContatos)

menuManutencao = Menu(barra,tearoff=0)
menuManutencao.add_command(label='Novo', command=imprimir)
menuManutencao.add_command(label='Pesquisar', command=imprimir)
menuManutencao.add_command(label='Deletar', command=imprimir)
barra.add_cascade(label='manutenção',menu=menuManutencao)

app.config(menu=barra)
app.mainloop()