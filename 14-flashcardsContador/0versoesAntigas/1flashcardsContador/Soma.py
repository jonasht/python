class Soma:
    
    def __init__(self):
        self.numeroDeCartas = list()
        
        
    def set_numeroDeCartas(self, numero):
        if numero == '':
            numero = '1'
            
        numero = numero[:]
        self.numeroDeCartas.extend(numero)
        
    def get_numeroDeCartas(self):
        return self.numeroDeCartas

    def ConverterPInt(self, converter):
        convertidos = []
        for c in converter:
            convertidos.append(int(c))
        
        return convertidos
    
    def Somar(self):
        return sum(self.ConverterPInt(self.get_numeroDeCartas()))
        
    