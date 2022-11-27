from tkinter import *
from tkinter import ttk
from fr_bts1 import Fr_bts1
from fr_bts2 import Fr_bts2
from fr_key import Fr_key
import uteis as u
from corFunc import formatar


class Fr(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)


        
        self.txt1 = Text(self)
        self.txt2 = Text(self)
        self.scbar1 = ttk.Scrollbar(self, orient=VERTICAL, command=self.txt1.yview)
        self.scbar2 = ttk.Scrollbar(self, orient=VERTICAL, command=self.txt2.yview)
        self.txt1.config(yscrollcommand=self.scbar1.set)
        self.txt2.config(yscrollcommand=self.scbar2.set)

        # chamando frames
        self.fr_bts1 = Fr_bts1(self, self)
        self.fr_bts2 = Fr_bts2(self, self)
        self.fr_key = Fr_key(self, self)

        # colocando widgets =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        # separetor
        self.spt = ttk.Separator(self, orient=VERTICAL)

        self.txt1.grid(row=1, column=1)
        self.fr_bts1.grid(row=2, column=1, sticky=NSEW, columnspan=3)
        self.fr_bts1.bt_cri.config(width=62)
        
        # key
        self.fr_key.grid(row=0, column=3)
        self.fr_key.etd.config(width=50)

        self.spt.grid(row=0, column=2, padx=5, pady=5, sticky=NS, rowspan=3)
        
        self.txt2.grid(row=1, column=3)
        self.fr_bts2.grid(row=2, column=3, sticky=NSEW, columnspan=3)
        self.fr_bts2.bt_cri.config(width=62)
        
        # colocando scroll bar
        self.scbar1.grid(row=1, column=0, sticky=NS)
        self.scbar2.grid(row=1, column=4, sticky=NS)
        self.txt1.bind('<KeyRelease>', self.put_color)
        self.txt2.bind('<KeyRelease>', self.put_color)

      
        
    def put_color(self, event):
        
        # txt =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        txt = self.txt1.get('1.0', END)
        txt = txt.split('\n')
        self.formatado = list()


        # pegando informacoes 
        for i, c in enumerate(txt):
            self.formatado.append(formatar(i, c)) 
                
        if self.fr_key.cbt_value.get():
            # colocando  
            for f1 in self.formatado:
                for f in f1:
                    self.txt1.tag_add(f['nome'], f['p1'], f['p2'])
                    self.txt1.tag_config(f['nome'], foreground=f['fg'])   
                    
        else:
            # tirando a cor
            for f1 in self.formatado:
                for f in f1:
                    self.txt1.tag_add(f['nome'], f['p1'], f['p2'])
                    self.txt1.tag_config(f['nome'], foreground='white') 


        
        # txt2 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        txt = self.txt2.get('1.0', END)
        txt = txt.split('\n')
        self.formatado = list()

        # pegando informacoes 
        for i, c in enumerate(txt):
            self.formatado.append(formatar(i, c)) 
                
        if self.fr_key.cbt_value.get():
            # colocando  
            for f1 in self.formatado:
                for f in f1:
                    self.txt2.tag_add(f['nome'], f['p1'], f['p2'])
                    self.txt2.tag_config(f['nome'], foreground=f['fg'])   
        else:       
                # colocando  
                for f1 in self.formatado:
                    for f in f1:
                        self.txt2.tag_add(f['nome'], f['p1'], f['p2'])
                        self.txt2.tag_config(f['nome'], foreground='white')   
            
        # self.formatado_old = self.formatado.copy


    def criptar(self):
        txt = self.txt1.get(1.0, END)
        self.txt1_string = txt

        key, token = u.criptar(txt)

        self.del_txt2()
        self.txt2.insert(END, token)

        self.txt2_string = token

        self.fr_key.etd.delete(0, END)
        self.fr_key.etd.insert(0, key)
        


    def del_etd(self):
        pass
        self.key_etd.delete(0, END)
        
    def del_txt1(self):
        self.txt1.delete(1.0, END)
    
    def del_txt2(self):
        self.txt2.delete(1.0, END)

        
    def descriptar(self):
        txt = self.txt2.get(1.0, END)
        self.txt2_string = txt

        key = self.fr_key.etd.get()

        txt = u.descriptar(key, txt)

        self.del_txt1()
        self.txt1.insert(END, txt)
        self.txt2_string = txt


if __name__ == '__main__':
    app = Tk()


    # Create a style
    style = ttk.Style(app)

    # Import the tcl file
    app.tk.call('source', './forest_ttk_theme/forest-dark.tcl')

    # Set the theme with the theme_use method
    style.theme_use("forest-dark")

    Fr(app).pack()
    from sys import exit
    # app.bind('q', exit)

    app.mainloop()
