import requests
from tkinter import EW, Tk, ttk
class Fr(ttk.Frame):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.fr_up = ttk.Frame()
        self.texto = ttk.Label(self.fr_up, text="Clique no botão para atualizar as cotações de moedas")
        self.botao = ttk.Button(self.fr_up, text="Atualizar", command=self.pegar_cotacoes)
        # self.botao.config(width=20)
        self.texto.grid(row=0)
        self.botao.grid(row=1, sticky=EW)


        self.fr_ct = ttk.Frame()
        self.lbfr_dolar = ttk.LabelFrame(self.fr_ct, text='Dolar')
        self.lbfr_euro = ttk.LabelFrame(self.fr_ct, text='Euro')
        self.lbfr_BTC = ttk.LabelFrame(self.fr_ct, text='BTC')

        self.lb_dolar2 = ttk.Label(self.lbfr_dolar, text='')
        self.lb_euro2 = ttk.Label(self.lbfr_euro, text='')
        self.lb_BTC2 = ttk.Label(self.lbfr_BTC, text='')

        self.lb_dolar2.grid(row=0, column=0)
        self.lb_euro2.grid(row=1, column=0)
        self.lb_BTC2.grid(row=2, column=0)

        self.lbfr_dolar.grid(row=0, column=0, ipadx=20, sticky=EW)
        self.lbfr_euro.grid(row=1, column=0, ipadx=20, sticky=EW)
        self.lbfr_BTC.grid(row=2, column=0, ipadx=20, sticky=EW)
        
        self.fr_up.grid()
        self.fr_ct.grid(row=2)

        self.pegar_cotacoes()
    def pegar_cotacoes(self):
        requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

        requisicao_dic = requisicao.json()

        cotacao_dolar = requisicao_dic['USDBRL']['bid']
        cotacao_euro = requisicao_dic['EURBRL']['bid']
        cotacao_btc = requisicao_dic['BTCBRL']['bid']
        cotacao_dolar = 'R$ '+ str(cotacao_dolar.replace('.', ','))
        cotacao_euro = 'R$ '+ str(cotacao_euro.replace('.', ','))
        cotacao_btc = 'R$ '+ str(cotacao_btc)
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
    