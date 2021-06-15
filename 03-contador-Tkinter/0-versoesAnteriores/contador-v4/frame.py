from tkinter import *


class Interface(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self['bg']='Black'
        self.frame_principal = Frame(self, bg='black')
        
        self.label = Label(self.frame_principal, text="quantos segundos:", fg='green', bg='black')

        self.entrada = Entry(self.frame_principal, textvariable=0, borderwidth=5, bg='gray')

        self.lb_contagem = Label(self.frame_principal, fg='green', font='Times 100 bold', bg='black', text='0')

        self.bt = Button(self.frame_principal, fg='dark green', bg='gray', padx=25, pady=25,
                    text='Começar',
                    command=self.Contagem,
                    font='Arial 20 bold')

        self.bt_sair = Button(self.frame_principal, text='sair', fg='dark green', bg='gray', command=self.quit, font='Arial 20 bold')
        
        self.label.grid(row=0, column=0)
        self.entrada.grid(row=0, column=1)
        self.lb_contagem.grid(row=2, column=0, columnspan=2, sticky=W+E, pady=30)
        self.bt.grid(row=3, column=0, columnspan=2, sticky=W+E)
        self.bt_sair.grid(row=4, columnspan=2, sticky=W+E)

        
        self.frame_principal.pack()

        self.entrada.focus()
        self.ate=0
        self.segundos = None

    def Contagem(self):
        self.bt.config(state=DISABLED)
        
        if self.segundos == None:
            if self.entrada.get() != '':
                self.ate = int(self.entrada.get())
            else:
                self.entrada.delete(0, END)
                self.entrada.insert(0, 5)
                self.ate = 5
                
            self.segundos = -1 
        if self.segundos == self.ate:
            self.lb_contagem['text'] = 'Fim'
            
            
            self.segundos = None
            self.ate = 0
            self.bt.config(state=ACTIVE)
        else:
            self.segundos += 1
            self.lb_contagem['text'] = self.segundos
            self.lb_contagem.after(1000, self.Contagem)



if __name__ == '__main__':
    root = Tk()
    interface = Interface(root)
    interface.pack()

    root.mainloop()