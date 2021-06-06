
class Conta:
    def __init__(self, qtdCartas=30):
        self.qtdCartas = qtdCartas
        self.numRecomecar = 0
        self.numComecar = 0
        
    def somarRecomecar(self, numero):
        self.numRecomecar += numero
        
    def somarComecar(self, numero):
        self.numComecar += numero
        
    def get_numRecomecar(self):
        return self.numRecomecar
    
    def get_numComecar(self):
        return self.numComecar
    
    def get_total(self):
        return self.numRecomecar + self.numComecar
    def get_restanteDeCartas(self):
        return self.qtdCartas - self.get_total() 