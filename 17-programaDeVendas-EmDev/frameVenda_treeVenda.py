from tkinter import ttk
import tkinter as tk
from tkinter.constants import END, EW, NS, VERTICAL




class Fr_treeVenda(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Treeview produto ------------------------------------
        # definindo colunas
        self.colunas = ['cod', 'nome', 'marca', 'preco', 'x', 'total']
        self.tree_venda = ttk.Treeview(self, columns=self.colunas, show='headings')

        # definindo heading
        self.tree_venda.heading('cod', text='ID')
        self.tree_venda.heading('nome', text='Nome')
        self.tree_venda.heading('marca', text='Marca')
        self.tree_venda.heading('preco', text='Preço')
        self.tree_venda.heading('x', text='X')
        self.tree_venda.heading('total', text='Total')

        # definindo tamanho da coluna
        self.tree_venda.column('cod', width=20)
        self.tree_venda.column('nome', width=125)
        self.tree_venda.column('marca', width=90)
        self.tree_venda.column('preco', width=100)
        self.tree_venda.column('x', width=40)
        self.tree_venda.column('total', width=100)
        

        self.scroll = ttk.Scrollbar(self, orient=VERTICAL, command=self.tree_venda.yview)
        self.tree_venda.grid(row=1, column=0, columnspan=1)
        self.scroll.grid(row=1, column=1, rowspan=1, sticky=NS)

        # total de tudo 
        self.fr_total = ttk.Frame(self)
        self.total = 0
        self.lb_total = ttk.Label(self.fr_total, text='Total:')
        self.lb_totalInfo = ttk.Label(self.fr_total, text='----')
        
        self.lb_total.grid(row=0, column=0)
        self.lb_totalInfo.grid(row=0, column=1)

        self.fr_total.grid(row=2, column=0)


    def editar_dados(self) -> None:
        print(self.codigo)
        if self.codigo != '':


            codigo = self.codigo

            qtd =self.etd_qtd.get()
            preco =self.etd_preco.get()
            
            # add dados =-=-=-=-=-=-=-=-=-=-=-=-=
            print('codigo:', codigo)
            # print('nome:', nome)
            # print('marca:', marca)
            print('qtd:', qtd)
            print('preco:', preco)


            self.deletar_tree()
            self.mostrar_tree()


 
    def item_selected(self, event):
        for selected_item in self.tree_venda.selection():
            item = self.tree_venda.item(selected_item)
            record = item['values']

            print(record)
            
            self.codigo = record[0]
            self.inserir_dados()
        
    def digitar_evento(self, event):
        variavel = event.widget.get()
        print(variavel)
        # deletar tree view
        self.deletar_tree()

        # mostrar treeview com a palavra digitada
        self.mostrar_tree(palavras=variavel)
        
    def deletar_tree(self):
        # deletar toda a tree view
        self.tree_venda.delete(*self.tree_venda.get_children()) 
    def adicionar(self, d):
        self.total = float(self.total) + float(d[5])
        self.tree_venda.insert('', END, values=d)
        
        self.lb_totalInfo.config(text=f'{self.total:.2f}')
        
if __name__ == '__main__':
    root = tk.Tk()
    frame  = Fr_treeVenda(root)
    frame.pack()
    d = [1, 'celular', 'sony', 2000.0, 1, 2000.0]
    frame.adicionar(d)
    
    d = [1, 'celular', 'sony', 1000.0, 2, 2000.0]
    frame.adicionar(d)
    
    root.geometry('800x800')

    root.mainloop()