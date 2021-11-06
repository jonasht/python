from tkinter import *
import tkinter as tk
from tkinter import ttk
from colorama.ansi import Fore
import uteis as u



class FrAcesso(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.txt_estahAtivo = [True, False]
        self.controller = controller
        self.login = ''
        

        self.bt_logout = ttk.Button(self, text='log out', command=self.logout)
        self.bt_logout.pack(side=RIGHT)
        
        
        self.lb_login = ttk.Label(self, text='login:')
        self.lb_login.pack(side=LEFT)
        
        self.fr_msg = ttk.Frame(self)
        self.lb_msg = ttk.Label(self.fr_msg, text='mensagem:')
        
        self.txt_msg = Text(self.fr_msg, width=30, height=10)


        self.bt_editar = ttk.Button(self.fr_msg, text='Editar', command=self.editar)

        
        self.lb_msg.grid(row=0, column=1)

        self.txt_msg.grid(row=1)
        self.bt_editar.grid(row=2)
        
        self.fr_msg.pack()

        self.limpar_txt()
        # desativando o textbox
        msg = u.get_msg(self.login)
        self.txt_msg.insert(END, msg)
        self.txt_msg.config(state=DISABLED)
    
    def limpar_txt(self):
        self.txt_msg.delete('1.0', END)
        
    def set_login(self, login):
        self.login = login
        msg = f'bem vindo {self.login}'
        # self.lb_login.config(text=msg)
        
        
        
    def get_login(self):
        return self.login
    
    def logout(self):
        self.controller.show_frame('FrLogin')

    def editar(self):
        print('ativo:', self.txt_estahAtivo)
        # print('msg do banco de dados:', msg)
        
        if self.txt_estahAtivo[0]:
            print(Fore.GREEN, 'ativo', Fore.RESET)
            u.update_msg(self.login, self.txt_msg.get('1.0', END))
            self.txt_msg.config(state=NORMAL)
        else:
            msg = u.get_msg(self.login)
            self.txt_msg.insert(END, msg)
            self.txt_msg.config(state=DISABLED)
            print(Fore.RED, 'nao ativo', Fore.RESET)
            
        self.txt_estahAtivo.reverse()
        
        print('fim')
    def testar(self):
        print('teste')
        self.txt_msg.config(state=DISABLED)


if __name__ == '__main__':
    root = Tk()

    FrAcesso(root, None).pack()
    root.geometry('400x300')
    root.mainloop()
    
    # from main import Principal
    # root = Principal()
    # root.mainloop()