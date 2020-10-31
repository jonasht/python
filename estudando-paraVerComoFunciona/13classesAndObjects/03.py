def l (): print("="*30)

class User:
    def __init__(self, nome_completo, aniversario):
        self.nome = nome_completo
        self.aniversario = aniversario

        nome_pieces = nome_completo.split(' ')
        self.primeiro_nome = nome_pieces[0]
        self.sobrenome = nome_pieces[-1]
        
        
l()       
user = User("dove des brwan".title(), '012343')
print(user.nome)
print(user.primeiro_nome)
print(user.sobrenome)
print(user.aniversario)
l()