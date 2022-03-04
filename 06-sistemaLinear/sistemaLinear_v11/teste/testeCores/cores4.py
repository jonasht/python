import imp
from tkinter import *
from sys import exit
from corFunc import formatar

conta2x2 = 'x2y=5\n3x-5y=4'
class App(Tk):
    def __init__(self):
        super().__init__()

        self.text = Text(self, width=20, height=10)
        self.text.config(font='arial 20 bold')
        # self.text.insert(END, conta2x2)
        self.text.pack()
        self.text.config(background='black', foreground='white')
        
        # evento sair
        self.bind('q', self.q_evento)

        #
        self.bind('<KeyRelease>', self.event)
         
        
    def event(self, event):
        if self.text.get(1.0, END):
            self.put_color()
    def put_color(self):
        conta = self.text.get('1.0', END)
        print('c:', conta)
        conta = conta.split('\n')
        print(conta)
        formatado = list()
        
        # pegando informacoes 
        
        for i, c in enumerate(conta):
            formatado.append(formatar(i, c)) 
        print('f:', formatado)
        # colocando  
        for f1 in formatado:
            for f in f1:
                self.text.tag_add(f['nome'], f['p1'], f['p2'])
                self.text.tag_config(f['nome'], foreground=f['fg'])        

    def q_evento(self, event):
        exit()





if __name__ == '__main__':
    root = App()
    root.mainloop()