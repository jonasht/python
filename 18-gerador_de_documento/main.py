import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap import font, Window

from frames.cnpj import Fr_CNPJ
from frames.cpf import Fr_cpf
from frames.cnh import Fr_CNH
from frames.cns import Fr_CNS
from frames.pis import Fr_PIS
from frames.certidao import Fr_Certidao
from frames.RENAVAM import Fr_RENAVAM
from frames.tituloEleitoral import Fr_TituloEleitoral


class GeradorMain(Window):
    def __init__(self):
        super().__init__()
        # self.geometry('550x500')
        self.title('Gerador de Documentos')

        
        # lb tituo 
        self.lb_titulo = ttk.Label(self, text='Gerador de documentos | aperte q para sair')
        self.lb_titulo.configure(font='times 15 bold', foreground='dark gray')

        # definindo frames left right =-=-=-=-=-=-=-=-=-=-=-=-=
        self.fr_left = ttk.Frame(self)
        self.fr_right = ttk.Frame(self)
        
        self.fr_cpf = Fr_cpf(self)
        self.fr_cnpj = Fr_CNPJ(self)
        self.fr_cnh = Fr_CNH(self)
        
        self.fr_cns = Fr_CNS(self)
        self.fr_pis = Fr_PIS(self)
        
        self.fr_certidao = Fr_Certidao(self)

        self.fr_tituloEleitoral = Fr_TituloEleitoral(self)
        self.fr_renavam = Fr_RENAVAM(self)
        

        self.fr_cpf.  grid(row=0, column=0, padx=10, pady=7)
        self.fr_cnpj. grid(row=1, column=0, padx=10, pady=7)
        self.fr_cns.  grid(row=0, column=1, padx=10, pady=7)
        self.fr_pis.  grid(row=1, column=1, padx=10, pady=7)
        
        self.fr_certidao.  grid(row=2, column=0, padx=10, pady=7, columnspan=2)
        self.fr_renavam.  grid(row=2, column=2, padx=10, pady=7)

        
        self.fr_tituloEleitoral.grid(row=1, column=2, padx=10, pady=7)
        self.fr_cnh.  grid(row=0, column=2, padx=10, pady=7)
        self.lb_titulo.grid(row=3, column=0, columnspan=3)
        
        self.bind('q', lambda x: self.quit())
        

#? colocar esse jeito de main eh regra 
def main():
    root = GeradorMain()
    root.style.theme_use('darkly')
    root.mainloop()
    
if __name__ == '__main__':
    main()

    
        
