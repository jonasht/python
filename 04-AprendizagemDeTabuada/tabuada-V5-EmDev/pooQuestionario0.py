
# Utilizando programação orientada a objetos, 
# escreva uma classe simples para representar o objeto CARRO, com: 
# Dois atributos privados,
# um construtor que receba o valor dos dois atributos, 
# dois métodos públicos que retorne o valor dos dois atributos. 
# Utilize a linguagem que mais lhe agrada. *


class Carro:
    def __init__(self):
        self.pessoaPrivada1 # privado
        self.pessoaPrivada2 # privado
        


    def construtor(self, pessoaPrivada1, pessoaPrivada2):
        self.pessoaPrivada1 = pessoaPrivada1
        self.pessoaPrivada2 = pessoaPrivada2
        
    def get_metadoPublico1(self):
        return self.pessoaPrivada1
    
    def get_metadoPublico2(self):
        return self.pessoaPrivada2