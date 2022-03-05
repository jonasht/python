from cryptography.fernet import Fernet
def criptar(msg):

    key = Fernet.generate_key()
    # print('key')

    f = Fernet(key)
    
    token = f.encrypt(msg.encode())
    # print('token:', token)
    
    # convertendo para string
    key = key.decode('utf-8')
    token = token.decode('utf-8')
    return key, token

def decriptar(key, token):
    key = key.encode()
    token = token.encode()
    f = Fernet(key)
    msg = f.decrypt(token)
    
    msg = msg.decode('utf-8')

    return msg
    
print('=-'*30+'=')

while True:
    print('qualquer tecla para sair ou s')
    op = input(f'1 criptografar\n2 decritografar\nop: ')


    match op:
        case '1':
            msg = input('msg: ')
            key, token = criptar(msg)
            print('key:', key)
            print('token:\n', token)

        case '2':
            key = input('key:')
            token = input('token:')

            decriptado = decriptar(key=key, token=token)
            print('=-'*30+'=')
            print('mensagem:\n', decriptado)

        case _:
            print('saindo ...')
            break
        

