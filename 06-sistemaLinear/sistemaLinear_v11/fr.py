from tkinter import ttk
from tkinter import *

import uteis as u
import exemplo as ex
from corFunc import formatar, cores
import pyperclip


class Fr(ttk.Frame):
    def __init__(self, parent, con):
        super().__init__(parent)
        self.con = con
        
        # frames left right
        self.fr_left = ttk.Frame(self)
        self.separetor = ttk.Separator(self, orient=HORIZONTAL)
        self.fr_right = ttk.Frame(self)
        
        self.bt_colar = ttk.Button(self.fr_left, text='Colar', command=self.colar)
        self.txt = Text(self.fr_left, width=40, height=10)
        self.txt.config(font='times 20 italic bold')
        self.bt_calcular = ttk.Button(self.fr_left, text='Calcular',  
                             command=self.calcular_evento)
        self.bt_limpar = ttk.Button(self.fr_left, text='Limpar', command=self.delete_evento)
        self.txt_solve =  Text(self.fr_left, width=40, height=10)
        self.txt_solve.config(font='times 15 italic bold')
        
        self.bt_copiar = ttk.Button(self.fr_left, text='Copiar', command=self.copiar)
        
        self.bt_colar.grid(row=0, column=0, sticky=NSEW, columnspan=2, pady=4)
        self.txt.grid(row=1, column=0, sticky=NSEW, columnspan=2)
        self.bt_calcular.grid(row=2, column=1, sticky=NSEW, pady=5, padx=4, ipadx=40)
        self.bt_limpar.grid(row=2, column=0, sticky=NSEW, pady=5, padx=2)

        self.txt_solve.grid(row=3, column=0, sticky=NSEW, columnspan=2)
        self.bt_copiar.grid(row=4, column=0, sticky=NSEW, columnspan=2, pady=4)
        
        # label frame
        self.lbfr = ttk.Labelframe(self.fr_right, text='Exemplos', border=25)

        self.bt_e1x1 = ttk.Button(self.lbfr, text='1x1', command=self.bt_1x1evento)
        self.bt_e2x2 = ttk.Button(self.lbfr, text='2x2', command=self.bt_2x2evento)
        self.bt_e3x3 = ttk.Button(self.lbfr, text='3x3', command=self.bt_3x3evento)
        self.bt_e4x4 = ttk.Button(self.lbfr, text='4x4', command=self.bt_4x4evento)
        
        self.bt_e1x1.grid(padx=8, pady=6)
        self.bt_e2x2.grid(padx=8, pady=6)
        self.bt_e3x3.grid(padx=8, pady=6)
        self.bt_e4x4.grid(padx=8, pady=6)
        
        self.lbfr.pack(anchor=W)
        
        self.fr_left.grid(row=0, column=0, padx=15, pady=15)
        self.separetor.grid(row=0, column=1, sticky=NS)
        self.fr_right.grid(row=0, column=2, padx=15, pady=15, sticky=NSEW)
        
        self.txt.bind('<KeyRelease>', self.txt_event)
        
        # default teste
        # self.bt_3x3evento()
        # self.calcular_evento()

    def colar(self):
        txt = pyperclip.paste()
        self.txt.delete(1.0, END)
        self.txt.insert(1.0, txt)
        
    def copiar(self):
        txt = self.txt_solve.get(1.0, END)
        pyperclip.copy(txt)
        
    def txt_event(self, event):
        if self.txt.get(1.0, END):
            self.put_color()
            
    def put_color(self):
        conta = self.txt.get('1.0', END)
        conta = conta.split('\n')
        self.formatado = list()

        # pegando informacoes 
        for i, c in enumerate(conta):
            self.formatado.append(formatar(i, c)) 
            
        # colocando  
        for f1 in self.formatado:
            for f in f1:
                self.txt.tag_add(f['nome'], f['p1'], f['p2'])
                self.txt.tag_config(f['nome'], foreground=f['fg'])   


    def delete_evento(self):
        self.txt.delete(1.0, END)
        # self.lb_solucao.config(text='')
        self.txt_solve.delete(1.0, END)
        
        
    def del_txtSolve(self):
        self.txt_solve.delete(1.0, END)
       
       
    def bt_1x1evento(self):
        self.delete_evento()
        self.txt.insert(1.0, ex.conta1x1)
        self.put_color()
        
        
    def bt_2x2evento(self):
        self.delete_evento()
        self.txt.insert(1.0, ex.conta2x2)
        self.put_color()
        
        
    def bt_3x3evento(self):
        self.delete_evento()
        self.txt.insert(1.0, ex.conta3x3)
        self.put_color()
        
        
    def bt_4x4evento(self):
        self.delete_evento()
        self.txt.insert(1.0, ex.conta4x4) 
        self.put_color()
        
    def calcular_evento(self):
        # deletando txt_solve
        self.del_txtSolve()

        conta = self.txt.get(1.0, END)
        solve = u.calcular(conta)
        txt_solve = ''
        
        for c, v in solve.items():
            txt_solve += f'     {c} = {v}\n'
        
        self.txt_solve.insert(1.0, txt_solve)
        
        solve_split = txt_solve.split('\n')
        
        t_split = list()
        for i, c in enumerate(solve_split):
            t_split.append(formatar(i, c)) 
        
        # colocando  
        for i, t in enumerate(t_split):
            for tt in t:
                self.txt_solve.tag_add(tt['nome'], tt['p1'], tt['p2'])
                self.txt_solve.tag_config(tt['nome'], foreground=cores[i], font='times 30 italic bold')   


  


if __name__ == '__main__':
    from main import main
    main()
