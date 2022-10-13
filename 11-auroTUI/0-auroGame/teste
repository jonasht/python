from interface import *
import numpy as np

class M2:
    interface = Interface()
    def __init__(self, tamanhoDaLista, tempoDeAtraso, charPixel = '  '):
        
        self.interface.set_tamanhoDaLista(tamanhoDaLista)
        self.interface.set_tempoDeAtraso(tempoDeAtraso)
        self.interface.set_charPixel(charPixel)

    
    def Maneira2(self):
                
        for _ in np.arange(len(self.interface.lista)):
            for i in np.arange(len(self.interface.lista)):

                if i+1 == len(self.interface.lista):
                    continue
                else:
                    if self.interface.lista[i] > self.interface.lista[i+1]:
                        guardarNumero = self.interface.lista[i]
                        self.interface.lista[i] = self.interface.lista[i+1]
                        self.interface.lista[i+1] = guardarNumero
                        self.interface.converterPMostrar(n=i+1, oque=2)
                        self.ultimoColumaPApagar = i+1
                        
            for i in reversed(np.arange(len(self.interface.lista))):

                if i+1 == len(self.interface.lista):
                    continue
                else:
                    if self.interface.lista[i] > self.interface.lista[i+1]:
                        guardarNumero = self.interface.lista[i]
                        self.interface.lista[i] = self.interface.lista[i+1]
                        self.interface.lista[i+1] = guardarNumero
                        self.interface.converterPMostrar(n=i, oque=3)                        
                        self.ultimoColumaPApagar = i
                        
                        
        # redefinindo a lista - a ultima coluna luminada para redefinir/apagar 
        self.interface.converterPMostrar(n=self.ultimoColumaPApagar, oque=1)                        

