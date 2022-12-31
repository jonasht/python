import tkinter as tk
from tkinter import NE, NSEW, ttk
from tkinter.constants import BOTH, DISABLED, END, EW, N, NORMAL, NW, RIGHT, LEFT, S, TOP, W, X, Y
from colorama.ansi import Fore
import uteis as u



class FrAcesso(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # frames =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        self.fr_cima = ttk.Frame(self)

        self.lb_login = ttk.Label(self.fr_cima, text='login:')
        
        self.bt_logout = ttk.Button(self.fr_cima, text='log out', command=self.logout)
        self.lb_login.grid(row=0, column=0, padx=3, pady=6)
        self.bt_logout.grid(row=0, column=1, sticky=EW, padx=3, pady=6)
        
        self.lbfr_msg = ttk.Labelframe(self, text='Mensagem')
        self.txt_msg = tk.Text(self.lbfr_msg)
        self.bt_editar = ttk.Button(self.lbfr_msg, text='Editar', command=self.editar)

        self.txt_msg.grid(row=0, padx=7, pady=6, sticky=NSEW)
        self.bt_editar.grid(row=1, padx=3, pady=3, sticky=NSEW)

        # self.lbfr_msg.grid(row=1, column=0, padx=3, pady=6, sticky=EW, columnspan=2)
        self.fr_cima.pack(anchor=NE, padx=12)

        self.lbfr_msg.pack(anchor='center')
        self.lbfr_msg.config(padding=3)



        


    def limpar_txt(self):
        self.txt_msg.delete('1.0', END)
    
    
    def display(self, id):
        self.id = id
        data = u.get_dataById(id)
        

        msg_login = f'bem vindo {data["nome"].title()} {data["sobrenome"].title()}'
        
        self.lb_login.config(text=msg_login)
        
        msg = data['frase']
        # print('mensagem de texto:', msg)
        
        
        self.txt_msg.config(state=NORMAL)
        if msg:
            self.txt_msg.insert(END, msg)
        else:
            self.limpar_txt()    
            
        self.txt_msg.config(state=DISABLED, bg='lightgray')
        
        

        
        

    def logout(self):
        # self.controller.show_frame('FrLogin')
        self.txt_msg.config(state=NORMAL)
        self.limpar_txt()
        self.controller.show_login()

    def editar(self):


        if self.txt_msg['state'] != 'normal':
            self.txt_msg.config(state=NORMAL)
            self.bt_editar.config(text='OK')
            
            self.txt_msg.config(bg='white')
        else:
            self.txt_msg.config(state=DISABLED)
            self.bt_editar.config(text='Editar')

            self.txt_msg.config(bg='lightgray')

        msg_data = u.get_dataById(self.id)['frase']
        msg = self.txt_msg.get('1.0', END)

        if not msg_data or msg_data != msg[:-1]:
            print('entrou')
            u.update_msg(self.id, msg)

        
       

    def insert_inTxt(self, msg):
        self.limpar_txt()
        self.txt_msg.insert(END, msg)



if __name__ == '__main__':

    # root = tk.Tk()

    # fr = FrAcesso(parent=root, controller=None)

    # fr.display(1)
    
    # fr.pack()
    # root.geometry('800x800')
    # root.mainloop()
    import main
    
    root = main.Principal()
    
    root.show_acesso(2)
    root.mainloop()

    
