import ttkbootstrap as ttk
from ttkbootstrap import Window
from ttkbootstrap.constants import *
from downloadVideo import download_yt
import pyperclip as ppc


class Root(Window):
    def __init__(self):

        
        super().__init__()
        # frame botoes
        self.fr_bts = ttk.Frame(self)

        self.txt = ttk.Text(self, height=50) 
        self.lb_title = ttk.Label(self, text='coloque os links para download:', font=('Arial', 20, 'bold'))

        self.bt_paste = ttk.Button(self.fr_bts, text='Colar',  width=24, padding=65)
        self.bt_download = ttk.Button(self.fr_bts, text='Download', bootstyle=SUCCESS, width=20, padding=80)
        self.bt_delete = ttk.Button(self.fr_bts, text='Apagar', bootstyle=DANGER, width=24, padding=65)

        self.bt_paste.configure(command=self.cmd_paste)
        self.bt_download.configure(command=self.cmd_download)
        self.bt_delete.configure(command=self.cmd_delete)
        
        
        self.lb_aviso = ttk.Label(self, text='', font=('Arial', 15))
        self.lb_msg = ttk.Label(self, text='esc to exit', font=('Arial', 23, 'bold'))

        self.lb_title.grid(row=0, column=0)
        self.txt.grid(row=1, column=0, padx=20, pady=20, rowspan=2)
        
        self.lb_msg.grid(row=2, column=1, padx=10)
        self.lb_aviso.grid(row=3, column=0, columnspan=1)

        # colocando botoes
        self.bt_paste.grid(row=0, column=0, pady=10)
        self.bt_download.grid(row=1, column=0, pady=10)
        self.bt_delete.grid(row=2, column=0, pady=10)

        self.fr_bts.grid(row=1, column=1, rowspan=1)

        # esc para sair
        self.bind('<Escape>', lambda x: self.quit())
        
    def cmd_paste(self):
        txt = self.txt.get(1.0, END)
        paste = ppc.paste()

        if txt[-2:] == '\n\n' or txt=='\n':
            self.txt.insert(END, paste+'\n')
        else:
            self.txt.insert(END, '\n'+paste+'\n')
            


    def cmd_delete(self):
        self.txt.delete(1.0, END)

    
    def cmd_download(self):
        txt = self.txt.get(1.0, END)
        txt = txt.split('\n')
        

        while '' in txt: txt.remove('')
        if txt:
      
            for i, t in enumerate(txt):
            
                    msg = download_yt(t)
            
            if msg:
                self.lb_aviso.configure(text='download feito com sucesso', bootstyle=SUCCESS)
            else:
                self.lb_aviso.configure(text='ocorreu um erro', bootstyle=DANGER)
                
        else:
            self.lb_aviso.configure(text='por favor coloque um link de video do youtube', bootstyle=WARNING)

def main():
    root = Root()
    root.title('download video youtube')
    root.style.theme_use('darkly')
    root.bind('q', lambda x: root.quit())
    root.mainloop()

if __name__ == '__main__':
    main()
    