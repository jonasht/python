import requests
from tkinter import BOTTOM, EW, Tk
import ttkbootstrap as ttk
from PIL import ImageTk, Image


class Fr(ttk.Frame):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        
        self.fr_up = ttk.Frame(self)
        self.texto = ttk.Label(self.fr_up, text='Clique no botão para atualizar as cotações de moedas', bootstyle='info')
        self.botao = ttk.Button(self.fr_up, text='Atualizar', command=self.get_cotacao, bootstyle='success')
        self.texto.grid(row=0, pady=6)
        self.botao.grid(row=1, sticky=EW, pady=6)


        self.fr_ct = ttk.Frame(self)
        self.lbfr_dolar = ttk.LabelFrame(self.fr_ct, text='Dolar', bootstyle='info')
        self.lbfr_euro = ttk.LabelFrame(self.fr_ct, text='Euro', bootstyle='info')
        self.lbfr_BTC = ttk.LabelFrame(self.fr_ct, text='Bitcoin', bootstyle='info')
        
        # img =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        self.img_dolar = ImageTk.PhotoImage(Image.open('./img/dolar.png'))
        self.lbimg_dolar = ttk.Label(self.lbfr_dolar, image=self.img_dolar)
        self.lbimg_dolar.grid(row=0, column=0, padx=30)
        
        self.img_euro = ImageTk.PhotoImage(Image.open('./img/euro.png'))
        self.lbimg_euro = ttk.Label(self.lbfr_euro, image=self.img_euro)
        self.lbimg_euro.grid(row=0, column=0, padx=30)
        
        self.img_BTC = ImageTk.PhotoImage(Image.open('./img/bitcoin.png'))
        self.lbimg_BTC = ttk.Label(self.lbfr_BTC, image=self.img_BTC)
        self.lbimg_BTC.grid(row=0, column=0, padx=30)
        # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=        

        self.lb_dolar = ttk.Label(self.lbfr_dolar, text='', font='Arial 16 bold')
        self.lb_euro2 = ttk.Label(self.lbfr_euro, text='', font='Arial 16 bold')
        self.lb_BTC2 = ttk.Label(self.lbfr_BTC, text='', font='Arial 16 bold')

        self.lb_dolar.grid(row=0, column=1, pady=6, padx=10)
        self.lb_euro2.grid(row=0, column=1, pady=6, padx=10)
        self.lb_BTC2.grid(row=0, column=1, pady=6, padx=10)

        self.lbfr_dolar.grid(row=0, column=0, ipadx=30, sticky=EW, pady=6)
        self.lbfr_euro.grid(row=1, column=0, ipadx=20, sticky=EW, pady=6)
        self.lbfr_BTC.grid(row=2, column=0, ipadx=20, sticky=EW, pady=6)
        
        self.fr_up.grid()
        self.fr_ct.grid(pady=10)

        self.get_cotacao()
    def get_cotacao(self) -> None:
        requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

        requisicao_dic = requisicao.json()

        cotacao_dolar = requisicao_dic['USDBRL']['bid']
        cotacao_euro = requisicao_dic['EURBRL']['bid']
        cotacao_btc = requisicao_dic['BTCBRL']['bid']
        cotacao_dolar = 'R$ '+ str(cotacao_dolar.replace('.', ','))
        cotacao_euro = 'R$ '+ str(cotacao_euro.replace('.', ','))
        cotacao_btc = 'R$ '+ str(cotacao_btc)
        self.lb_dolar.config(text=cotacao_dolar)
        self.lb_euro2.config(text=cotacao_euro)
        self.lb_BTC2.config(text=cotacao_btc)
def main():
    
    window = Tk()
    fr = Fr(window)
    window.resizable(width=False, height=False)
    fr.pack()
    lb_exit = ttk.Label(window, text='esc/q para sair\nEsc/q to exit', bootstyle='warning')
    lb_exit.pack(side=BOTTOM)

    window.bind('q', lambda x: window.destroy())
    window.bind('<Escape>', lambda x: window.destroy())
    
    # grid()
    
    window.geometry('600x500')
    window.title('Cotação de Moedas')


    window.mainloop()
    
if __name__ == '__main__':
    main()
    