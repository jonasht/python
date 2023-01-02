from tkinter import TOP, Tk, ttk
import customtkinter as ctk
from fr_alternativas import Fr_alternativas
from fCards import Fcards


cards_test = {
    'green': 'verde',
    'yellow': 'amarelo',
    'black': 'preto',
    'blue': 'azul',
    'red': 'vermelho',
    'white': 'branco'
    }

class Fr_cards(ctk.CTkFrame):
    def __init__(self, parent, con):
        super().__init__(parent)
        self.con = con

        
        self.lb = ctk.CTkLabel(self, text='teste', font=('Helvetica', 300))
        self.lb.grid()

        
        

class App(ctk.CTk):
    def __init__(self):
        
        super().__init__()
        
        self.cards_test = {
                'green': 'verde',
                'yellow': 'amarelo',
                'black': 'preto',
                'blue': 'azul',
                'red': 'vermelho',
                'white': 'branco'
        }
        
        self.fcards = Fcards(self.cards_test)
        self.fcards.start()


        self.fr_cards = Fr_cards(self, self)
        self.fr_cards.pack()
        
        self.fr_alternativas = Fr_alternativas(self, self)
        self.fr_alternativas.pack(pady=30)

        self.aviso = ctk.CTkLabel(self, text='teste')
        self.aviso.pack()

        # mostrando fcards
        self.show()
        
        # mostrando resposta
    
    def set_resposta(self, resposta):

        print(resposta, type(resposta))
        print('-------------------')
      
        print(self.alternativas[resposta])
        
        if self.fcards.set_resposta(self.alternativas[resposta]):
            print('certo')
            self.aviso.configure(text='certo', fg_color='green')
        else:
            print('errado')
            self.aviso.configure(text='errado', fg_color='red')

        self.show()
        

    def show(self):
        
        if not self.fcards.working():
            self.aviso.configure(text='acabou!!!', fg_color='blue')
        else:
            self.fr_cards.lb.configure(text=self.fcards.get_pergunta())
            self.alternativas = self.fcards.get_alternativa()
            self.fr_alternativas.display(self.alternativas)
            print('resposta:', cards_test[self.fcards.perguntasShuffle[0]])
        

    
    
        
if __name__ == '__main__':
    app = App()
    app.geometry('800x800')
    app.mainloop()
