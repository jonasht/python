from cpf_cnpj import CpfCnpj, Documento
from random import randint

# cpf1 = CpfCnpj('01234567890')
cnpj1 = Documento.cria_documento('62298916412239')

print('cnpj1:', cnpj1)

cpf1 = Documento.cria_documento('36820366108')
print('cpf1:', cpf1)

# cpf2 = range() for i in range(1, 12)
cpf2 = '123245678941'
cpf2 = Documento.cria_documento(cpf2)
print('cpf2:', cpf2)