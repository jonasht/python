from tkinter import ttk
import tkinter as tk
from tkinter.constants import DISABLED, END, EW, NORMAL
from func.venda import add_venda, add_entregas



class Fr_finalizacao(ttk.Frame):
    def __init__(self, parent, con):
        super().__init__(parent)
        self.con = con

        
        self.chbt_cpf = ttk.Checkbutton(self, text='CPF na nota', command=self.chbt_cpfEvento)
        self.etd_cpf = ttk.Entry(self)
        self.chbt_entrega = ttk.Checkbutton(self, text='É para a entrega')
        self.bt_finalizar = ttk.Button(self, text='Finalizar', command=self.finalizar_evento)
        
        self.chbt_cpf.grid(padx=5, pady=2)
        self.etd_cpf.grid(padx=5, pady=2)
        self.chbt_entrega.grid(padx=5, pady=2)
        self.bt_finalizar.grid(sticky=EW)
        
        self.chbt_cpf.state(['!alternate'])
        self.chbt_entrega.state(['!alternate'])
        
        
    def chbt_cpfEvento(self):
        cpf = self.con.dados_cliente[2]

        if 'selected' in self.chbt_cpf.state():
            self.etd_cpf.config(state=NORMAL)
            self.etd_cpf.delete(0, END)
            self.etd_cpf.insert(0, cpf)
        else:
            self.etd_cpf.delete(0, END)
            self.etd_cpf.config(state=DISABLED)

        
    def finalizar_evento(self):

        # gravar dados

        # pegar items/produtos p registrar a venda 
        dados_produto = self.con.get_itemsTreeVenda()
        dados_cliente = self.con.dados_cliente
        total = self.con.get_totalTreeVenda()
        
        # adicionando no banco de dados a venda 
        add_venda(
            dados_cliente=dados_cliente,
            dados_produto=dados_produto,
            total=total
        )

        self.etd_cpf.delete(0, END)
        self.chbt_cpf.state(['!selected'])
        self.chbt_entrega.state(['!selected'])
        self.con.apagar_tudo()
                    
if __name__ == '__main__':
    root = tk.Tk()
    frame = Fr_finalizacao(root, root)
    frame.pack()
    root.geometry('500x500')
    root.mainloop()