
from tkinter import *
import func_produtos as funcP

class FrPesquisarProduto(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.fr_direita = Frame(self)
        
        self.frame = Frame(self)
        self.lbfr = LabelFrame(self.frame, text='Pesquisar')
        
        self.lb_pesquisar = Label(self.lbfr, text='codigo/nome:')
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
        self.etd_pesquisar.insert(0, 'celular')
        
    def pesquisar(self):
        # self.apagar_botoes()
        opcao = str(self.etd_pesquisar.get())
        
        
        self.fr_lista = Frame(self)
        self.fr_lista.pack()    

        dados = funcP.pesquisar(opcao)
        
        print(dados)
        if len(dados) > 1:
            self.bt_lista = []
            
            
            for i, dado in enumerate(dados):
                self.bt_lista.append(Button(self.fr_lista, text=f'nome:{dado[1]}',
                                    command=lambda dado=dado: self.mostrar_dadosLista(dado),
                                    
                                    width=25))
                self.bt_lista[i].grid()
        
 
        else:
            pass
            # self.mostrar_telaCompra(dados[0])
        
    def mostrar_dadosLista(self, dados):
        print('=-=-')
        print('dados:', dados)
        
        # colocando labels de tela dados
        self.lb_dados = Label(self.fr_direita, text=f'''
                         id:{dados[0]}
                         nome:{dados[1]}
                         marca:{dados[2]}
                         quantidade:{dados[3]}
                         valor:{dados[4]}
                         descrição:{dados[5]}
                        ''')
        self.lb_dados.grid()
        
if __name__ == '__main__':
    root = Tk()
    frame = FrPesquisarProduto(root)
    frame.pack()
    root.geometry('600x500')
    root.mainloop()