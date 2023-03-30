
class Conta:
    def __init__(self, qtdCartas=30):
        self.qtdCartas = qtdCartas
        self.recomecar = list()
        self.comecar = list()
        
    def somarRecomecar(self, numero):
        self.recomecar.append(numero)
        
    def somarComecar(self, numero):
        self.comecar.append(numero)
        
    def get_recomecar(self):
        return self.recomecar
    def get_totalRecomecar(self):
        return sum(self.recomecar)

    def get_comecar(self):
        return self.comecar
    
    def get_totalComecar(self):
        return sum(self.comecar)


    def get_total(self):
        return sum(self.recomecar) + sum(self.comecar)
    def get_restanteDeCartas(self):
        return self.qtdCartas - self.get_total() 
    

if __name__ == '__main__':
    from main import main
    main()