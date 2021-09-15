from tkinter import *
import uteis as u

class FrameCompra(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.botao_qtd = 0
        
        self.lbfr_dado = LabelFrame(self, text='Dados', width=50)
        self.lbfr_venda = LabelFrame(self, text='Venda')
        
        self.lb_dados = Label(self.lbfr_dado, text='')
        
        self.lb_qtd = Label(self.lbfr_venda, text='Quantidade:')
        self.etd_qtd = Entry(self.lbfr_venda, width=5)
        self.bt_menos = Button(self.lbfr_venda, text='-', command=self.botao_menos_on)
        self.bt_mais = Button(self.lbfr_venda, text='+', command=self.botao_mais_on)
        self.lb_valor = Label(self.lbfr_venda, text='R$', fg='green')
        self.etd_valor = Entry(self.lbfr_venda, width=5)


        self.bt_finalizar = Button(self, text='Finalizar', command=self.botao_finalizar_on)
        self.lb_aviso = Label(self, text='nenhum aviso')
        self.lb_dados.grid(row=1, column=2)
        
        
        self.lb_qtd.grid(row=2, column=2)
        self.etd_qtd.grid(row=3, column=2)
        self.bt_menos.grid(row=3, column=1)
        self.bt_mais.grid(row=3, column=3)
        self.lb_valor.grid(row=4, column=1)
        self.etd_valor.grid(row=4, column=2)

        self.lbfr_dado.grid(padx=25)
        self.lbfr_venda.grid()
        self.bt_finalizar.grid(row=2)
        self.lb_aviso.grid(row=3)
        self.etd_qtd.insert(0, 1)
        
    def set_dados(self, dado):
        self.dado = dado
        print('set dados:', dado)
    def botao_finalizar_on(self):
        finalizar = []
        
        
        nome_produto = self.dado[1]
        codigo_produto = self.dado[0]
        valor_produto = self.dado[2]
        qtd_vendida = str(self.etd_qtd.get())
        total = float(valor_produto) * float(qtd_vendida)
        total_sugerido = str(float(self.etd_valor.get()))

        print('produto:', nome_produto, 'codigo:', codigo_produto, 'valor:', valor_produto, 'qtd vendida:', qtd_vendida,'total:', total, 'total sugerido:', total_sugerido)

    def botao_menos_on(self):
        valor = int(self.etd_qtd.get())
        self.etd_qtd.delete(0, END)
        if valor != 0:
            valor-=1
        self.etd_qtd.insert(0, str(valor))
        self.etd_valor.delete(0, END)
        self.etd_valor.insert(0, (str(float(self.dado[2]) * float(valor))))
        
        
    def botao_mais_on(self):
        valor = int(self.etd_qtd.get())
        self.etd_qtd.delete(0, END)
        valor+=1
        self.etd_qtd.insert(0, str(valor))
        self.etd_valor.delete(0, END)
        self.etd_valor.insert(0, (str(float(self.dado[2]) * float(valor))))
        
        
class FrameVenda(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.fr_ladoEsquerdo = Frame(self)
        self.fr_ladoDireito = Frame(self)
        self.fr_pesquisar = Frame(self.fr_ladoEsquerdo)
        
        self.lb_pesquisar = Label(self.fr_pesquisar, text='Pesquisar codigo/nome:')
        self.etd_pesquisar = Entry(self.fr_pesquisar)
        self.bt_pesquisar = Button(self.fr_pesquisar, text='pesquisar', command=self.pesquisar)
        self.lb_pesquisar.grid(row=0, column=0)
        self.etd_pesquisar.grid(row=1, column=0)
        self.bt_pesquisar.grid(row=1, column=1)
        self.fr_pesquisar.grid(row=0, column=0)
        

        self.fr_lista = Frame(self.fr_ladoEsquerdo)
        self.fr_lista.grid(row=1, column=0)
        self.frCompra = FrameCompra(self.fr_ladoDireito)

        self.fr_ladoEsquerdo.pack(side=LEFT, anchor=NW)
        self.fr_ladoDireito.pack(side=RIGHT, anchor=NE)
        
        # defaut ---------------------------- apagar depois
        # self.etd_pesquisar.insert(0, 'a')
        # self.pesquisar()

    def pesquisar(self):
        self.apagar_botoes()
        opcao = str(self.etd_pesquisar.get())
        
        
        self.fr_lista = Frame(self.fr_ladoEsquerdo)
        self.fr_lista.grid(row=1, column=0)        

        dados = u.pesquisar(opcao)

        print(dados)
        if len(dados) > 1:
            self.bt_lista = []
            
            
            for i, dado in enumerate(dados):
                if dado[3] != 0:
                    self.bt_lista.append(Button(self.fr_lista, text=f'nome:{dado[1]}\nid:{dado[0]}, quatidade:{dado[3]}\ntamanho:{dado[4]}, cor:{dado[5]}preço:{dado[2]}', 
                                        command=lambda dado=dado: self.mostrar_telaCompra(dado),
                                        
                                        width=25))
                    self.bt_lista[i].grid()
                else:
                    self.bt_lista.append(Button(self.fr_lista, text=f'nome:{dado[1]}\nid:{dado[0]}, quatidade:{dado[3]}\ntamanho:{dado[4]}, cor:{dado[5]}preço:{dado[2]}', 
                                        bg='#FFA07A',
                                        width=25))
                    self.bt_lista[i].grid() 
        else:
            self.mostrar_telaCompra(dados[0])
                
    def mostrar_telaCompra(self, dado):
        self.frCompra.grid()
        self.frCompra.lb_dados.config(text=f'nome:{dado[1]}\nid:{dado[0]}, quatidade:{dado[3]}\ntamanho:{dado[4]}, cor:{dado[5]}preço:{dado[2]}')
        preco = str(dado[2])
        self.frCompra.set_dados(dado)
        self.frCompra.etd_valor.delete(0, END)
        self.frCompra.etd_valor.insert(0, preco)

    def apagar_botoes(self):
        self.fr_lista.destroy()
        self.frCompra.forget()
    
if __name__ == '__main__':
    root = Tk()
    frame = FrameVenda(root)
    root.geometry('500x500')
    frame.grid()
    root.mainloop()