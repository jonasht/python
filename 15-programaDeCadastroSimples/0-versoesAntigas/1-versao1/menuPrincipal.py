from tkinter import *



def ehNumero(n):
    try:
        int(n)
        return True
    except:
        return False

def cadastrar():
    print("entrando em cadastro")
    import interfaceCadastro
    
def Pesquisar():
    print('entrando em pesquisar')
    import interfaceDados


root = Tk()
root.geometry('200x200+450+300')


lb_telaPricipal = Label(root, text='tela principal', fg='blue').pack(pady=2)
bt_cadastrar    = Button(root, text='cadastrar', width=15, command=cadastrar).pack(pady=2)
# bt_conta        = Button(root, text='conta', width=15, command=Pesquisar).pack(pady=2)
bt_pesquisar    = Button(root, text='pesquisar', width=15, command=Pesquisar).pack(pady=2)

root.mainloop()