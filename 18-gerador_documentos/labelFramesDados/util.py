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
        'ẑ':'z',
        'ź':'z',

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

    nome = nome.lower()
    nome = remove_things(nome)
    nome_list = nome.split(' ')
    
    q = [True, False]
    if choice(q):
        nome = nome_list[0] + '.' + nome_list[-1]
    elif choice(q):
        nome = nome_list[0][:2] + '.' + nome_list[-1]
    elif choice(q):
        nome = nome_list[0][:3] + '.' + nome_list[-1]
    elif choice(q):
        nome = nome_list[0][:2] + '.' + nome_list[-1][:2]
    elif choice(q):
        nome = nome_list[0][:2] + '.' + nome_list[-1][:3]
    else:
        nome = nome_list[0] + nome_list[-1]
        # nome = ''.join(nome_list)
    print(date)

    
    print('data:', date)
    if False:
        nome = nome + date

    print(nome)
    email = f'{nome}@{choice(EMAIL_LINKS)}'
    return email

def gen_date():
    dia = str(randint(0, 30))
    mes = str(randint(1, 12))
    ano = str(randint(1990, 2010))
    return f'{dia}/{mes}/{ano}'


if __name__ == '__main__':
    nome = 'jórge henrique teixeira'
    data = gen_date()
    email = generate_email(nome, data)
    print(email)
    import email
    email.main()