from tkinter import CENTER, TOP, Tk, ttk
from fr_alternativas import Fr_alternativas
from fCards import Fcards
from fr_image import Fr_image



class Fr_play(ttk.Frame):
    def __init__(self, parent, con=None):
    

        
        super().__init__(parent)
        self.con = con
        
        self.cards_test = {
            'R-12': 'Proibido trânsito de bicicletas',
            'R-13': 'Proibido trânsito de tratores e máquinas de obras',
            'R-14': 'Peso bruto total máximo permitido',
            'R-15': 'Altura máxima permitida',
            'R-16': 'Largura máxima permitida',
            'R-17': 'Peso máximo permitido por eixo',
            'R-18': 'Comprimento máximo permitido',
            'R-19': 'Velocidade máxima permitida',
            'R-20': 'Proibido acionar buzina ou sinal sonoro',
            'R-21': 'Alfândega',
            'R-22': 'Uso obrigatório de corrente',
            'R-29': 'Proibido trânsito de pedestres',
            'R-30': 'Pedestre, ande pela esquerda',
            'R-31': 'Pedestre, ande pela direita',
            'R-32': 'Circulação exclusiva de ônibus',
            'R-33': 'Sentido de circulação na rotatória',
            'R-34': 'Circulação exclusiva de bicicletas',
            'R-35A': 'Ciclista, transite à esquerda',
            'R-35B': 'Ciclista, transite à direita',
            'R-36A': 'Ciclistas à esquerda, pedestres à direita',
            'R-36B': 'Pedestres à esquerda, ciclistas à direita',
            'R-37': 'Proibido trânsito de motocicletas, motonetas e ciclomotores',
            'R-38': 'Proibido trânsito de ônibus',
            'R-39': 'Circulação exclusiva de caminhão',
        }
        
        self.tamanho_img = (600, 600)
        self.fcards = Fcards(self.cards_test)
        self.fcards.start()

        self.fr_image = Fr_image(self, self, self.tamanho_img)
        self.fr_image.pack()
        
        self.fr_alternativas = Fr_alternativas(self, self)
        self.fr_alternativas.pack(pady=30)

        self.aviso = ttk.Label(self, text='teste')
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
            self.aviso.configure(text='certo', foreground='green')
        else:
            print('errado')
            self.aviso.configure(text='errado', foreground='red')

        self.show()
        

    def show(self):
        
        if not self.fcards.working():
            self.aviso.configure(text='acabou!!!', foreground='blue')
        else:
            # self.fr_cards.lb.configure(text=self.fcards.get_pergunta())
            self.fr_image.display(self.fcards.get_pergunta())

            self.alternativas = self.fcards.get_alternativa()
            self.fr_alternativas.display(self.alternativas)
            print('resposta:', self.cards_test[self.fcards.perguntasShuffle[0]])
        

class App(Tk):
    def __init__(self):
        super().__init__()
        ttk.Label(text='teste').pack()


        
    
        
if __name__ == '__main__':
    app = App()
    fr = Fr_play(app)
    fr.pack(anchor=CENTER)
    app.geometry('800x800')
    app.mainloop()

