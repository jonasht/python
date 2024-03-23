import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap import font, Window

from labelframes.cnpj import Fr_CNPJ
from labelframes.cpf import Fr_cpf
from labelframes.cnh import Fr_CNH
from labelframes.cns import Fr_CNS
from labelframes.pis import Fr_PIS
from labelframes.certidao import Fr_Certidao
from labelframes.RENAVAM import Fr_RENAVAM
from labelframes.tituloEleitoral import Fr_TituloEleitoral

from PIL import Image, ImageTk

import utils as u


class GeradorMain(Window):
    def __init__(self):
        super().__init__()
        # vars
        self.var = ttk.BooleanVar()

        self.title('Gerador de Documentos')
        # frame dos documentos principal
        self.fr_doc = ttk.Frame(self)

        
        # lb tituo 
        self.lb_titulo = ttk.Label(self.fr_doc, text='Gerador de documentos | aperte q para sair')
        self.lb_titulo.configure(font='times 15 bold', foreground='dark gray')

        
        # button config
        self.image = Image.open('./img/contexto.png')
        self.image = self.image.resize((25, 25), Image.LANCZOS)

        self.imagetk = ImageTk.PhotoImage(self.image)
        self.bt_config = ttk.Button(self, image=self.imagetk, command=self.open_topbar, bootstyle=LINK)
        #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

        # botao gerar tudo 
        self.bt_gerar = ttk.Button(self.fr_doc, text='gerar tudo',bootstyle=SUCCESS, command=self.cmd_gerarTudo)

        # checkbutton colocar maskara em tudo
        self.chb_mask = ttk.Checkbutton(self.fr_doc, text='Mask Tudo', variable=self.var, command=self.chb_event, bootstyle="success-round-toggle")

        # definindo labelframes =-=-=-=-=-=-=-=-=-=-=-=-=
        self.fr_cpf = Fr_cpf(self.fr_doc)
        self.fr_cnpj = Fr_CNPJ(self.fr_doc)
        self.fr_cnh = Fr_CNH(self.fr_doc)
        self.fr_cns = Fr_CNS(self.fr_doc)
        self.fr_pis = Fr_PIS(self.fr_doc)
        self.fr_certidao = Fr_Certidao(self.fr_doc)
        self.fr_tituloEleitoral = Fr_TituloEleitoral(self.fr_doc)
        self.fr_renavam = Fr_RENAVAM(self.fr_doc)
        

        # button config
        self.bt_config.grid(row=0, column=3)

        self.fr_cpf.  grid(row=0, column=0, padx=10, pady=4)
        self.fr_cnpj. grid(row=1, column=0, padx=10, pady=4)
        self.fr_cns.  grid(row=0, column=1, padx=10, pady=4)
        self.fr_pis.  grid(row=1, column=1, padx=10, pady=4)
        
        self.fr_certidao.  grid(row=2, column=0, padx=10, pady=4, columnspan=2, sticky=EW)
        self.fr_renavam.  grid(row=2, column=2, padx=10, pady=4)

        
        self.fr_tituloEleitoral.grid(row=1, column=2, padx=10, pady=7)
        self.fr_cnh.  grid(row=0, column=2, padx=10, pady=7)
        self.lb_titulo.grid(row=3, column=0, columnspan=2)
        self.bt_gerar.grid(row=3, column=2, sticky=EW, padx=10, pady=7)
        self.chb_mask.grid(row=4, column=2, sticky=E)
        
        # colocando a frame doc principal
        self.fr_doc.grid(row=1, column=0)
        # colocan bt config
        self.bt_config.grid(row=0, column=0, sticky=E)

        self.bind('q', lambda x: self.quit()) 
        self.bind('<Escape>', lambda x: self.quit()) 
        # set theme config


        self.style.theme_use(u.get_configTheme())
        self.change_theme_lbTitle()
    def chb_event(self):
        var = True if self.var.get() else False
        self.fr_cpf.var.set(var)
        self.fr_cnpj.var.set(var)
        self.fr_cnh.var.set(var)
        self.fr_cns.var.set(var)
        self.fr_pis.var.set(var)
        self.fr_certidao.var.set(var)
        self.fr_tituloEleitoral.var.set(var)
        self.fr_renavam.var.set(var)

        # atualizar tela das entradas das frames com a mask
        self.fr_cpf.chbt_Evento()
        self.fr_cnpj.chbt_Evento()
        self.fr_cnh.chbt_Evento()
        self.fr_cns.chbt_Evento()
        self.fr_pis.chbt_Evento()
        self.fr_certidao.chbt_Evento()
        self.fr_tituloEleitoral.chbt_Evento()
        self.fr_renavam.chbt_Evento()

    # muda state widgets normal|disabled de labelframes
    def state_all(self, states:str=NORMAL) -> None:
        self.fr_cpf.state(states)
        self.fr_cnpj.state(states)
        self.fr_cnh.state(states)
        self.fr_cns.state(states)
        self.fr_pis.state(states)
        self.fr_certidao.state(states)
        self.fr_tituloEleitoral.state(states)
        self.fr_renavam.state(states)

        self.bt_gerar.config(state=states)
        self.chb_mask.config(state=states)
    def cmd_gerarTudo(self):
        self.fr_cpf.gerar()
        self.fr_cnpj.gerar()
        self.fr_cnh.gerar()
        self.fr_cns.gerar()
        self.fr_pis.gerar()
        self.fr_certidao.gerar()
        self.fr_tituloEleitoral.gerar()
        self.fr_renavam.gerar()
    def change_theme_lbTitle(self):
        pass
        theme = self.style.theme_use()
        if theme == 'darkly' or theme == 'cyborg':
            self.lb_titulo.configure(font='times 14 bold', foreground='dark gray')
        elif theme == 'solar':
            self.lb_titulo.configure(font='times 14 bold', foreground='white')
        else:
            self.lb_titulo.configure(font='times 14 bold', foreground='gray')
# superhero
    def change_theme(self, event):
        theme = self.cb.get()
        self.change_theme_lbTitle()
        self.style.theme_use(theme)
        u.set_configTheme(self.style.theme_use())
        
    def open_topbar(self):
        # disabled bt config
        self.bt_config.config(state=DISABLED)
        # self.state_all(DISABLED)
        
        
        # func close toplevel
        def on_toplevel_close(event=None):

            # if not str(event.widget).startswith(str(self.toplevel)):
                # self.toplevel.destroy()
            
            self.toplevel.destroy()
            self.bt_config.config(state=NORMAL)
            # self.state_all(NORMAL)

        self.toplevel = ttk.Toplevel(self)
        self.toplevel.place_window_center()
        self.toplevel.geometry('300x180')
        self.toplevel.title('Config Tema')

        self.fr_theme = ttk.Label(self.toplevel)

        self.lb_theme = ttk.tk.Label(self.fr_theme, text='Tema:')


        cb_list = self.style.theme_names()
        self.cb = ttk.Combobox( self.fr_theme, values=cb_list, state=READONLY, bootstyle=SUCCESS)
        self.cb.set(cb_list[cb_list.index(self.style.theme_use())])

        self.bt_toplevelQuit = ttk.Button(self.toplevel, text='Fechar')

        self.bt_toplevelQuit.config(command=on_toplevel_close)
        self.bt_toplevelQuit.config(bootstyle=DANGER)
        self.lb_theme.grid(row=0, column=0)
        self.cb.grid(row=0, column=1)
        self.fr_theme.pack(side=TOP)
        self.bt_toplevelQuit.pack(side=BOTTOM, fill=BOTH)
        
        self.cb.bind('<<ComboboxSelected>>', self.change_theme)
        self.toplevel.bind('<Escape>', on_toplevel_close)

        # Definindo a função para fechar o Toplevel
        self.toplevel.protocol('WM_DELETE_WINDOW', on_toplevel_close)
        # se clicar fora do top level>fechar
        self.bind('<FocusIn>', on_toplevel_close)

def main():
    window = GeradorMain()
    window.place_window_center()
    # window.style.theme_use('darkly')
    window.mainloop()
    
if __name__ == '__main__':
    main()

    
        
