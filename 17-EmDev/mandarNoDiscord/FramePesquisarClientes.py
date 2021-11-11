
from tkinter import *
import func_clientes as funcC

class FrPesquisarCliente(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.fr_direita = Frame(self)
        
        self.frame = Frame(self)
        self.lbfr = LabelFrame(self.frame, text='Pesquisar')
        
        self.lb_pesquisar = Label(self.lbfr, text='id/nome:')
        self.lb_pesquisar.grid(row=0, column=0)
        
        self.etd_pesquisar = Entry(self.lbfr)
        self.etd_pesquisar.grid(row=0, column=1)
        
        self.bt_pesquisar = Button(self.lbfr, text='pesquisar', command=self.pesquisar)

        self.bt_pesquisar.grid(row=0, column=2)
        
        
        # dados =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        
        self.lbfr_dados = LabelFrame(self.frame, text='Dados')
        self.lbfr.grid(row=0, column=0)
        self.lbfr_dados.grid(row=0, column=1)
        
        self.frame.pack()
        
        
        self.fr_direita.pack(side=RIGHT)

        
        # config defaults =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        self.etd_pesquisar.insert(0, 'rodrigo')
        
    def pesquisar(self):
        # self.apagar_botoes()
        opcao = str(self.etd_pesquisar.get())
        
        
        self.fr_lista = Frame(self)
        self.fr_lista.pack()    

        dados = funcC.pesquisar(opcao)
        
        print(dados)
        if len(dados) > 1:
            print('entrou')
            self.bt_lista = []
            
            
            for i, dado in enumerate(dados):
                self.bt_lista.append(Button(self.fr_lista, text=f'nome:{dado[1]}',
                                    command=lambda dado=dado: self.mostrar_dadosLista(dado),
                                    
                                    width=25))
                self.bt_lista[i].grid()
        
 
        else:
            self.mostrar_dadosLista(dados[0])
            # self.mostrar_telaCompra(dados[0])
        
    def mostrar_dadosLista(self, dados):
        print('=-=-')
        print('dados:', dados)
        
        # colocando labels de tela dados
        self.lb_dados = Label(self.fr_direita, text=f'''
                         id: {dados[0]}
                         nome: {dados[1]}
                         cpf: {dados[2]}
                         UF: {dados[3]}
                         cidade: {dados[4]}
                         rua: {dados[5]} N:{dados[6]}
                         Fone: {dados[7]}
                         E-mail: {dados[8]}
                        ''')
        self.lb_dados.grid()
        
if __name__ == '__main__':
    root = Tk()
    frame = FrPesquisarCliente(root)
    frame.pack()
    root.geometry('600x500')
    root.mainloop()