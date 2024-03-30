from faker import Faker
from random import choice
from datetime import datetime

FAKE = Faker('pt_br')



class DadosPessoa:
    emails_links = ['yahoo.com', 'yahoo.com.br',
                        'outlook.com', 'outlook.com.br',
                        'hotmail.com', 'hotmail.com.br',
                        'gmail.com', 'icloud.com', 'aol.com',
                        'live.com', 'bol.com.br', 'uol.com.br',
                        'terra.com.br', 'ig.com.br',
                        'r7.com', 'zipmail.com.br',
                        'protonmail.com','yandex.com']
    def __init__(self) -> None:
        
        self.generate()
    

    def generate(self) -> None:
        def create_email(nome:str) -> str:
            return nome.replace(' ', '') +'@' + choice(self.emails_links)
        
        self.nome = FAKE.name()
        self.fone = FAKE.phone_number()
        self.email = create_email(self.nome)
        self.data_nascimento = FAKE.date_of_birth(minimum_age=18, maximum_age=70, ).strftime("%d/%m/%Y")
    


    def show(self) -> print:
        def l(qtd=30, oq='='):
            print(oq*qtd)
        l()
        print('              nome:', self.nome)
        print('          telefone:', self.fone)
        print('             email:', self.email)
        print('data de nascimento:', self.data_nascimento)
        l()




class DadosLocal:
    def __init__(self) -> None:
        self.generate()

    def generate(self):
        
        self.rua = FAKE.street_name()
        self.numero = FAKE.building_number()
        self.bairro = FAKE.neighborhood()
        self.cidade = FAKE.city()
        self.estado = FAKE.state_abbr()     

    def show(self):
        def l(qtd=30, oq='='):
            print(oq*qtd)
        l()
        print("   Rua:", self.rua)
        print("Número:", self.numero)
        print("Bairro:", self.bairro)
        print("Cidade:", self.cidade)
        print("Estado:", self.estado)
        l()

dadosP = DadosPessoa()
dadosL = DadosLocal()

dadosP.show()
dadosL.show()