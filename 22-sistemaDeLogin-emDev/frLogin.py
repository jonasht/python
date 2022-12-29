import tkinter as tk
from tkinter import ttk
from tkinter.constants import END, EW, X

import uteis as u
from colorama.ansi import Fore
from PIL import Image, ImageTk


class FrLogin(ttk.Frame):
    def __init__(self, parent, controller):
        
        super().__init__(parent)
        self.controller = controller
        
        # colocando imagem na tela =-=-=-=-=-=-=
        image = Image.open('./img/yellowdiamond.png')
        width = 132
        height = 142
        resize_image = image.resize((width, height))
        self.img = ImageTk.PhotoImage(resize_image)
        self.lb_img = ttk.Label(self, image=self.img).pack()
        
        
        self.lbfr_meio = ttk.LabelFrame(self, text='Login')
        
        self.lb_login = ttk.Label(self.lbfr_meio, text='login:')
        self.lb_senha = ttk.Label(self.lbfr_meio, text='Senha:')

        self.etd_login = ttk.Entry(self.lbfr_meio)
        self.etd_senha = ttk.Entry(self.lbfr_meio, show='*')

        self.lb_login.grid(row=0, column=0, pady=5)
        self.etd_login.grid(row=0, column=1, pady=5, padx=5)
        self.lb_senha.grid(row=1, column=0, pady=5)
        self.etd_senha.grid(row=1, column=1, pady=5, padx=5)

        self.bt_limpar = ttk.Button(self.lbfr_meio, text='Limpar')
        self.bt_entrar = ttk.Button(self.lbfr_meio, text='Entrar', command=self.acessar)
        self.bt_limpar.grid(row=2, column=0, padx=3, pady=4, sticky=EW)
        self.bt_entrar.grid(row=2, column=1, padx=3, pady=4, sticky=EW)

        self.lbfr_meio.pack(padx=3, pady=6)

        self.bt_cadastrar = ttk.Button(self, text='Cadastrar', width=34, command=self.controller.show_cadastro)
        self.bt_cadastrar.pack()

        self.lb_aviso = ttk.Label(self, text='')
        self.lb_aviso.pack()
 
        self.etd_login.focus()
        
        # configuracoes default
        self.etd_login.insert(0, 'jonas')
        self.etd_senha.insert(0, '123')

    def acessar(self):
        login = self.etd_login.get()
        senha = self.etd_senha.get()

        if login == '':
            self.lb_aviso.config(text='por favor insira o login')
        elif senha == '':
            self.lb_aviso.config(text='por favor insira o senha')
        
        
        print(login, senha)
        
        senhaDoSistema = u.get_senha(login)
        print('senhaDoSistema:', senhaDoSistema)


        if senhaDoSistema and senhaDoSistema == senha:
            print(Fore.GREEN+'acesso permitido', Fore.RESET)
            # self.controller.set_login(login)
            id = u.get_id(login)
            self.controller.show_acesso(id)

            
        else:
            print(Fore.RED+'acesso negado', Fore.RESET)
            self.lb_aviso.config(text='senha ou login invalido')
    

        
if __name__ == '__main__':
    import main
    main.main()
    # root = tk.Tk()
    # frame = FrLogin(root, None)
    # root.geometry('500x500')

    # frame.pack()
    # root.mainloop()

