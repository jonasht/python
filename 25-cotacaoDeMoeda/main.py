from turtle import color
import requests
from tkinter import Tk, ttk
class Fr(ttk.Frame):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.fr_up = ttk.Frame()
        self.texto = ttk.Label(self.fr_up, text="Clique no botão para ver as cotações de moedas")
        self.botao = ttk.Button(self.fr_up, text="Buscar cotações", command=self.pegar_cotacoes)
        
        self.texto.grid(row=0)
        self.botao.grid(row=1)


        self.fr_ct = ttk.Frame()
        self.lb_dolar1 = ttk.Label(self.fr_ct, text='Dolar:')
        self.lb_dolar2 = ttk.Label(self.fr_ct, text='')
        self.lb_euro1 = ttk.Label(self.fr_ct, text='Euro:')
        self.lb_euro2 = ttk.Label(self.fr_ct, text='')
        self.lb_BTC1 = ttk.Label(self.fr_ct, text='BTC:')
        self.lb_BTC2 = ttk.Label(self.fr_ct, text='')

        self.lb_dolar1.grid(row=0, column=0)
        self.lb_dolar2.grid(row=0, column=1)
        self.lb_euro1.grid(row=1, column=0)
        self.lb_euro2.grid(row=1, column=1)
        self.lb_BTC1.grid(row=2, column=0)
        self.lb_BTC2.grid(row=2, column=1)
        
        self.fr_up.grid()
        self.fr_ct.grid(row=2)

    def pegar_cotacoes(self):
        requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

        requisicao_dic = requisicao.json()

        cotacao_dolar = requisicao_dic['USDBRL']['bid']
        cotacao_euro = requisicao_dic['EURBRL']['bid']
        cotacao_btc = requisicao_dic['BTCBRL']['bid']

        self.lb_dolar2.config(text=cotacao_dolar)
        self.lb_euro2.config(text=cotacao_euro)
        self.lb_BTC2.config(text=cotacao_btc)
def main():
    
    janela = Tk()
    fr = Fr(janela)
    fr.grid()
    janela.title("Cotação de Moedas")



    janela.mainloop()
if __name__ == '__main__':
    main()
    