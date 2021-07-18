print('\nfeito no windows, vscode\n\n')

class User:
    pass

user1 = User()
user1.primeiro_nome = "davi".title()
user1.sobrenome = 'kaili'.title()
print(user1.primeiro_nome)
print(user1.sobrenome)
print('='*30)
primeiro_nome = 'artur'.title()
sobrenome = 'clarke'.title()
print('='*30)
print(primeiro_nome, sobrenome)
print(user1.primeiro_nome, user1.sobrenome)
def l():print('='*30)

user2 = User()
user2.primeiro_nome = 'frank'.title()
user2.sobrenome = 'pul'.title()
l()
print(user2.primeiro_nome, user2.sobrenome)

user1.age = 37
user2.livro_favorito = '2001: a space odyssey'.title()
l()
print(user1.age, user1.livro_favorito)