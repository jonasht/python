from random import choice, randint
from faker import Faker
import re

FAKER = Faker('pt-br')

# links dos emails
EMAIL_LINKS= ['yahoo.com', 'yahoo.com.br',
                'outlook.com', 'outlook.com.br',
                'hotmail.com', 'hotmail.com.br',
                'gmail.com', 'icloud.com', 'aol.com',
                'live.com', 'bol.com.br', 'uol.com.br',
                'terra.com.br', 'ig.com.br', 'r7.com', 
                'zipmail.com.br','protonmail.com','yandex.com']

# remove palavras com acentos e siglas
def remove_things(word:str) -> str:
    chars = {
        'á':'a',
        'é':'e',
        'í':'i',
        'ó':'o',
        'ú':'u',
        'ñ':'n',
        'ỹ':'y',
        'ý':'y',
        'ã':'a',
        'ẽ':'e',
        'ĩ':'i',
        'õ':'o',
        'ũ':'u',
        'ç':'c',
        'à':'a',
        'è':'e',
        'ì':'i',
        'ò':'o',
        'ù':'u',
        'â':'a',
        'ê':'e',
        'î':'i',
        'ô':'o',
        'û':'u',
        'ŷ':'y',
        'ĉ':'c',
        'ŝ':'s',
        'ĵ':'j',
        

        'dra\.\s': '',
        'dr\.\s': '',
        'sr\.\s': '',
        'sra\.\s': '',
        'srta\.\s': '',
    }

    for k, v in chars.items():
        # print(k, v, '=', word)
        # print(k, v, '=', word)
        word = re.sub(k, v, word)
    return word

# gera um email utilizando nome
def generate_email(nome:str='', date:str=''):
    if not nome: nome = FAKER.name()

    nome = nome.lower()
    nome = remove_things(nome)
    nome = nome.split(' ')
    # print(nome)
    q:list = [True, False]
    if choice(q):
        if choice(q):
            for i, n in enumerate(nome):
                if choice(q) and i == 0:
                    nome[0] = n[:2]
                elif choice(q):
                    nome[i] = n[:4]
                else:
                    nome[i] = n[:3]
        elif choice(q):
            nome[0] = nome[0][:2]

    # data de nascimento
    
    date = date.split(('/' if '/' in date else '-'))
    if choice(q):
            date = date[0] if len(date[0]) == 4 else date[-1]
    else:
         date = ''
    #   -------------------
    
    if choice(q):
        nome = nome[0], nome[-1]
        nome = '.'.join(nome)
    else:
        nome = ''.join(nome)
    
    return nome +date+'@' + choice(EMAIL_LINKS)



def gen_date():
    dia = str(randint(0, 30))
    mes = str(randint(1, 12))
    ano = str(randint(1990, 2010))
    return f'{dia}/{mes}/{ano}'





# for i in range(200):
#     date = gen_date()
#     nome = FAKER.name()
#     email = generate_email(nome, date)
#     print('email:', email)
#     print(' nome:', nome)
#     print('----------------------')

for _ in range(10):
    email = generate_email()
    print('|>'+email+'<|')
    print('-'*len(email)+'----')

# nome = 'Dra. Letícia da Costa'
# email = generate_email(nome)
# print(email)
# nome = 'Sr. Daniel Rocha'
# email = generate_email(nome)
# print(email, nome)
# nome = 'Dr. Luiz Otávio da Costa'
# email = generate_email(nome)
# print(email, '|nome:' + nome)
# nome = 'Srta. Alice Sales'
# email = generate_email(nome)
# print(email, '|nome:' + nome)
# Ana Laura Rocha

