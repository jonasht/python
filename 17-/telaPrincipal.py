from tkinter import *

def cadastrar():
    print("entrando em cadastro")
def conta():
    print('entrando em conta')
    
root = Tk()
root.geometry('200x150+400+300')

lb_telaPricipal = Label(root, text='tela principal', fg='blue').pack(pady=2)
bt_cadastrar    = Button(root, text='cadastrar', width=15, command=cadastrar).pack(pady=2)
bt_conta        = Button(root, text='conta', width=15, command=conta).pack(pady=2)
bt_pesquisar    = Button(root, text='pesquisar', width=15).pack(pady=2)

root.mainloop()