

class M1:
    interface 
    def __init__(self, tamanhoDaLista, tempoDeAtraso):
        self.guardarNumero = 0
        
        self.interface.set_tamanhoDaLista(tamanhoDaLista)
        self.interface.set_tempoDeAtraso(tempoDeAtraso)

    
    def Maneira(self):
        
        for c in range(len(self.interface.lista)):
            for i in range(len(self.interface.lista)):

                if i+1 == len(self.interface.lista):
                    continue
                else:
                    if self.interface.lista[i] > self.interface.lista[i+1]:
                        guardarNumero = self.interface.lista[i]
                        self.interface.lista[i] = self.interface.lista[i+1]
                        self.interface.lista[i+1] = guardarNumero
                        self.interface.converterPMostrar(i+1)