
from tkinter import Label, ttk
import tkinter as tk
from tkinter.constants import BOTH, DISABLED, END, EW, LEFT, NORMAL, RIGHT, W
import func_clientes as funcC



class FrPesquisarCliente(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # definindo se o botao estah ativo ou nao
        self.btEstah_ativo = [False, True]
        # guardando nome
        self.nome = ''

        # definindo frames =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        self.fr_direita = ttk.Frame(self)
        self.fr_esquerdo = ttk.Frame(self)

        self.frame = ttk.Frame(self.fr_esquerdo)
        self.lbfr = ttk.LabelFrame(self.frame, text='Pesquisar')
        
        self.lb_pesquisar = ttk.Label(self.lbfr, text='id/nome:')
        self.lb_pesquisar.grid(row=0, column=0)
        
        self.etd_pesquisar = ttk.Entry(self.lbfr)
        self.etd_pesquisar.grid(row=0, column=1, sticky=EW)
        

        self.lb_id = ttk.Label(self.fr_direita, text='ID:')
        self.lb_nome = ttk.Label(self.fr_direita, text='Nome:')
        self.lb_cpf = ttk.Label(self.fr_direita, text='CPF:')
        self.lb_uf = ttk.Label(self.fr_direita, text='UF:')
        self.lb_cidade = ttk.Label(self.fr_direita, text='Cidade:')
        self.lb_rua = ttk.Label(self.fr_direita, text='Rua:')
        self.lb_fone = ttk.Label(self.fr_direita, text='Fone:')
        self.lb_email = ttk.Label(self.fr_direita, text='E-mail:')
        
        self.lb_idInfo = ttk.Label(self.fr_direita, text='')
        self.lb_nomeInfo = ttk.Label(self.fr_direita, text='')
        self.lb_cpfInfo = ttk.Label(self.fr_direita, text='')
        self.lb_ufInfo = ttk.Label(self.fr_direita, text='')
        self.lb_cidadeInfo = ttk.Label(self.fr_direita, text='')
        self.lb_ruaInfo = ttk.Label(self.fr_direita, text='')
        self.lb_foneInfo = ttk.Label(self.fr_direita, text='')
        self.lb_emailInfo = ttk.Label(self.fr_direita, text='')
        
        self.etd_id = ttk.Entry(self.fr_direita)
        self.etd_nome = ttk.Entry(self.fr_direita)
        self.etd_cpf = ttk.Entry(self.fr_direita)
        self.etd_uf = ttk.Entry(self.fr_direita)
        self.etd_cidade = ttk.Entry(self.fr_direita)
        self.etd_rua = ttk.Entry(self.fr_direita)
        self.etd_fone = ttk.Entry(self.fr_direita)
        self.etd_email = ttk.Entry(self.fr_direita)
        
        self.bt_editar = ttk.Button(self.fr_direita, text='Editar', command=self.editar_dados)


        self.lb_id.grid(row=0, column=0)
        self.lb_nome.grid(row=1, column=0)
        self.lb_cpf.grid(row=2, column=0)
        self.lb_uf.grid(row=3, column=0)
        self.lb_cidade.grid(row=4, column=0)
        self.lb_rua.grid(row=5, column=0)
        self.lb_fone.grid(row=6, column=0)
        self.lb_email.grid(row=7, column=0)
        
        self.lb_idInfo.grid(row=0, column=1)
        self.lb_nomeInfo.grid(row=1, column=1)
        self.lb_cpfInfo.grid(row=2, column=1)
        self.lb_ufInfo.grid(row=3, column=1)
        self.lb_cidadeInfo.grid(row=4, column=1)
        self.lb_ruaInfo.grid(row=5, column=1)
        self.lb_foneInfo.grid(row=6, column=1)
        self.lb_emailInfo.grid(row=7, column=1)
        
        # colocando botao editar
        self.bt_editar.grid(row=8, columnspan=2, sticky=EW)

        
        self.etd_id.grid(row=0, column=1)
        self.etd_nome.grid(row=1, column=1)
        self.etd_cpf.grid(row=2, column=1)
        self.etd_uf.grid(row=3, column=1)
        self.etd_cidade.grid(row=4, column=1)
        self.etd_rua.grid(row=5, column=1)
        self.etd_fone.grid(row=6, column=1)
        self.etd_email.grid(row=7, column=1)
                


        # Treeview =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        # definindo colunas
        self.colunas = ['id', 'nome', 'cpf', 'uf', 'cidade']
        self.treev = ttk.Treeview(self.fr_esquerdo, columns=self.colunas, show='headings' )

        # definindo heading
        self.treev.heading('id', text='ID')
        self.treev.heading('nome', text='Nome')
        self.treev.heading('cpf', text='CPF')
        self.treev.heading('uf', text='UF')
        self.treev.heading('cidade', text='Cidade')

        # definindo tamanho da coluna
        self.treev.column('id', width=10)
        self.treev.column('nome', width=150)
        self.treev.column('uf', width=50)
        self.treev.column('cidade', width=100)

        self.treev.grid(row=1, column=0, columnspan=3)
        self.lbfr.grid(row=0, column=0)
        

        self.frame.grid(row=0, column=0)
        # colocando frames 
        self.fr_esquerdo.pack(side=LEFT, fill=BOTH)
        self.fr_direita.pack(side=RIGHT, fill=BOTH)
        
        
        self.etd_pesquisar.bind('<KeyRelease>', self.digitar_evento)
        self.treev.bind('<<TreeviewSelect>>', self.item_selected)
        self.mostrar_tree()
        
        # desativando entradas/entry 
        self.etds_disabled()
        

  
    def etds_normal(self):
            self.etd_id.config(state=NORMAL)
            self.etd_nome.config(state=NORMAL)
            self.etd_cpf.config(state=NORMAL)
            self.etd_uf.config(state=NORMAL)
            self.etd_cidade.config(state=NORMAL)
            self.etd_rua.config(state=NORMAL)
            self.etd_fone.config(state=NORMAL)
            self.etd_email.config(state=NORMAL)        
    
    def etds_disabled(self):
            self.etd_id.config(state=DISABLED)
            self.etd_nome.config(state=DISABLED)
            self.etd_cpf.config(state=DISABLED)
            self.etd_uf.config(state=DISABLED)
            self.etd_cidade.config(state=DISABLED)
            self.etd_rua.config(state=DISABLED)
            self.etd_fone.config(state=DISABLED)
            self.etd_email.config(state=DISABLED)        
            
    def editar_dados(self):
        if self.nome != '':
            if self.btEstah_ativo[0]:
                self.etds_normal()
            else:
                print('bt false', self.btEstah_ativo)
                self.etds_disabled()  
        
            # trocando se estah ativo
            self.btEstah_ativo.reverse()
        
    def deletar_dados(self):
        self.etd_id.delete(0, END)
        self.etd_nome.delete(0, END)
        self.etd_cpf.delete(0, END)
        self.etd_uf.delete(0, END)
        self.etd_cidade.delete(0, END)
        self.etd_rua.delete(0, END)
        self.etd_fone.delete(0, END)
        self.etd_email.delete(0, END)
    
    def mostrar_dados(self, etdDesligada=True):
        if self.nome != '':
            dados = funcC.pesquisar(self.nome)
            print(dados)
            dados = dados[0]

            if self.btEstah_ativo[0]:
                self.deletar_dados()
                self.etd_id.insert(END, dados[0])
                self.etd_nome.insert(END, dados[1])
                self.etd_cpf.insert(END, dados[2])
                self.etd_uf.insert(END, dados[4])
                self.etd_cidade.insert(END, dados[5])
                self.etd_rua.insert(END, dados[6])
                self.etd_fone.insert(END, dados[7])
                self.etd_email.insert(END, dados[8])
            else:
                self.etds_normal()
                self.deletar_dados()
                
                self.etd_id.insert(END, dados[0])
                self.etd_nome.insert(END, dados[1])
                self.etd_cpf.insert(END, dados[2])
                self.etd_uf.insert(END, dados[4])
                self.etd_cidade.insert(END, dados[5])
                self.etd_rua.insert(END, dados[6])
                self.etd_fone.insert(END, dados[7])
                self.etd_email.insert(END, dados[8])
                self.etds_disabled()
                
    def item_selected(self, event):
        for selected_item in self.treev.selection():
            item = self.treev.item(selected_item)
            record = item['values']
            # show a message
            print(record)
            self.nome = record[1]
            self.mostrar_dados()
        
    def digitar_evento(self, event):
        variavel = event.widget.get()
        print(variavel)
        # deletar tree view
        self.deletar_tree()

        # mostrar treeview com a palavra digitada
        self.mostrar_tree(palavras=variavel)
        
    def deletar_tree(self):
        # deletar toda a tree view
        self.treev.delete(*self.treev.get_children()) 
    def mostrar_tree(self, palavras=''):

        dados = funcC.get_()
        print(dados)
        print('\n')

        dadosTree = list()
        for d in dados:
            # print(d[:5])
            dadosTree.append(d[:5])
            
            print('tree', dadosTree)
        
        print(dadosTree)
        
        if palavras != '':
            for d in dadosTree:
                # print(d)
                if palavras.lower() in d[1].lower():
                    self.treev.insert('', END, values=d)
        else:
            for d in dadosTree:
                self.treev.insert('', END, values=d)


if __name__ == '__main__':
    root = tk.Tk()
    frame = FrPesquisarCliente(root)
    frame.pack()
    root.geometry('1000x500')
    root.mainloop()