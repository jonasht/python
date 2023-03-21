import ttkbootstrap as ttk
from ttkbootstrap import Window
from ttkbootstrap.constants import *
from downloadVideo import download_yt




class Root(Window):
    def __init__(self):
        super().__init__()
        self.style.theme_use('darkly')
        self.title('download video youtube')
        self.txt = ttk.Text(self, height=50) 
        self.lb_title = ttk.Label(self, text='coloque os links para download:', font=('Arial', 20, 'bold'))
        self.bt_download = ttk.Button(self, text='Download', bootstyle=SUCCESS, padding=80)

        
        self.bt_download.configure(command=self.cmd_download)
        self.lb_aviso = ttk.Label(self, text='', font=('Arial', 15))
        self.lb_msg = ttk.Label(self, text='esc to exit', font=('Arial', 23, 'bold'))

        self.lb_title.grid(row=0, column=0)
        self.txt.grid(row=1, column=0, padx=20, pady=20, rowspan=2)
        self.bt_download.grid(row=1, column=1, padx=10)
        self.lb_msg.grid(row=2, column=1, padx=10)
        self.lb_aviso.grid(row=3, column=0, columnspan=1)

        # esc para sair
        self.bind('<Escape>', lambda x: self.quit())
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
if __name__ == '__main__':
    Root().mainloop()