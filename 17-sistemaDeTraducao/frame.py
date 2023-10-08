# from tkinter import Tk, Text, ttk
import ttkbootstrap as ttk
# from tkinter.constants import BOTH, BOTTOM, END, EW, RIGHT, TOP, LEFT, YES
# from googletrans import Translator
from ttkbootstrap.constants import *
import uteis as u

class Fr(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # self.values = ('pt', 'es', 'en')
        self.values = u.lang_values

        self.fr_esquerdo = ttk.Frame(self)
        self.fr_direito = ttk.Frame(self)


        self.lb_entrada = ttk.Label(self.fr_esquerdo, text='De:')
        self.combo_entrada = ttk.Combobox(self.fr_esquerdo, values=list(self.values.values()))
        self.txt1 = ttk.Text(self.fr_esquerdo)

        self.lb_saida = ttk.Label(self.fr_direito, text='Para:')
        self.combo_saida = ttk.Combobox(self.fr_direito, values=list(self.values.values()))
        self.txt2 = ttk.Text(self.fr_direito)

        # botao traduzir 
        self.bt_translate = ttk.Button(self, text='Traduzir', bootstyle=SUCCESS, command=self.traduzir)

        # definindo default
        self.combo_entrada.set('portugues')
        self.combo_saida.set('ingles')

        self.lb_entrada.grid(row=0, column=0, sticky=E)
        self.combo_entrada.grid(row=0, column=1, sticky=W, pady=5)
        self.txt1.grid(row=1, column=0, columnspan=2, sticky=EW)

        self.lb_saida.grid(row=0, column=0, sticky=E)
        self.combo_saida.grid(row=0, column=1, sticky=W, pady=5)
        self.txt2.grid(row=1, column=0, columnspan=2, sticky=EW)

        self.fr_esquerdo.grid(row=0, column=0, padx=2, pady=2)
        self.fr_direito.grid(row=0, column=1, padx=2, pady=2)
        self.bt_translate.grid(row=1, column=0, sticky=EW, columnspan=2, ipadx=1, ipady=5)
        
        self.lb_aviso = ttk.Label(self, text='', bootstyle=DANGER)
        self.lb_aviso.grid(row=2, column=0, columnspan=2)

        self.txt1.focus()
    def traduzir(self):
        msg_in = self.txt1.get(1.0, END)
        lang_in = u.get_key(u.lang_values, self.combo_entrada.get())
        lang_out = u.get_key(u.lang_values, self.combo_saida.get())
        # print(lang_in, lang_out)
        
        try:            
            traducao = u.traduzir(texto=msg_in, src=lang_in, target=lang_out)
            self.txt2.delete(1.0, END)
            self.txt2.insert(1.0, traducao)
            self.lb_aviso.config(text='')
        except:
            self.lb_aviso.config(text='pode estar com erro de conexao')
        
if __name__ == '__main__':
    import main
    main.main()