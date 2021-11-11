
from tkinter import ttk
import tkinter as tk
from tkinter.constants import END, RIGHT, W
import func_clientes as funcC



class FrPesquisarCliente(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.fr_direita = ttk.Frame(self)
        
        self.frame = ttk.Frame(self)
        self.lbfr = ttk.LabelFrame(self.frame, text='Pesquisar')
        
        self.lb_pesquisar = ttk.Label(self.lbfr, text='id/nome:')
        self.lb_pesquisar.grid(row=0, column=0)
        
        self.etd_pesquisar = ttk.Entry(self.lbfr)
        self.etd_pesquisar.grid(row=0, column=1)
        
        # self.bt_pesquisar = ttk.Button(self.lbfr, text='pesquisar', command=self.pesquisar)

        # self.bt_pesquisar.grid(row=0, column=2)
        
        
        # dados =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        
        self.lbfr_dados = ttk.LabelFrame(self.frame, text='Dados')
        self.lbfr.grid(row=0, column=0)
        self.lbfr_dados.grid(row=0, column=1)
        
        
        self.frame.pack()
        
        
        self.fr_direita.pack(side=RIGHT)

        
       

        # Treeview =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        # definindo colunas
        self.colunas = ['id', 'nome', 'cpf', 'uf', 'cidade']
        self.treev = ttk.Treeview(self, columns=self.colunas, show='headings' )

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

        self.treev.pack()
        
        self.etd_pesquisar.bind('<KeyRelease>', self.digitar_evento)
        
        self.mostrar_tree()
        
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
                    
    # def pesquisar(self):
    #     # self.apagar_botoes()
    #     opcao = str(self.etd_pesquisar.get())
        
        
    #     self.fr_lista = ttk.Frame(self)
    #     self.fr_lista.pack()    

    #     dados = funcC.pesquisar(opcao)
        
    #     print(dados)
    #     if len(dados) > 1:
    #         print('entrou')
    #         self.bt_lista = []
            
            
    #         for i, dado in enumerate(dados):
    #             self.bt_lista.append(ttk.Button(self.fr_lista, text=f'nome:{dado[1]}',
    #                                 command=lambda dado=dado: self.mostrar_dadosLista(dado),
                                    
    #                                 width=25))
    #             self.bt_lista[i].grid()
        
 
    #     else:
    #         self.mostrar_dadosLista(dados[0])
    #         # self.mostrar_telaCompra(dados[0])
        
        
    # def mostrar_dadosLista(self, dados):
    #     print('=-=-')
    #     print('dados:', dados)
        
    #     # colocando labels de tela dados
    #     self.lb_dados = ttk.Label(self.fr_direita, text=f'''
    #                      id: {dados[0]}
    #                      nome: {dados[1]}
    #                      cpf: {dados[2]}
    #                      UF: {dados[3]}
    #                      cidade: {dados[4]}
    #                      rua: {dados[5]} N:{dados[6]}
    #                      Fone: {dados[7]}
    #                      E-mail: {dados[8]}
    #                     ''')
    #     self.lb_dados.grid()
        

if __name__ == '__main__':
    root = tk.Tk()
    frame = FrPesquisarCliente(root)
    frame.pack()
    root.geometry('600x500')
    root.mainloop()