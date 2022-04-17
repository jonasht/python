from validate_docbr import CPF
from colorama.ansi import Fore
from random import randint

def validar_cpf(cpf):
    va = CPF()
    
    if cpf == '' or va.validate(cpf):
        print(Fore.GREEN+'cadastro feito com sucesso', Fore.RESET)
    else:
        print(Fore.RED+'erro de cpf', Fore.RESET)

cpf1 = ''
cpf2 = '123'
# cpf valido
cpf3 = '38218758100'

# outro cpf
cpf4 = '821875810d0'

 

validar_cpf(cpf1)
validar_cpf(cpf2)
validar_cpf(cpf3)
validar_cpf(cpf4)
