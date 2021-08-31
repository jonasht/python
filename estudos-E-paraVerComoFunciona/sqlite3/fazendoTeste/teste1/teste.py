import enum
from sqlite3.dbapi2 import ProgrammingError
import PegandoVariavel as v

pessoas = v.get_Pessoas()
print(pessoas)


print('--------------------------------------')

pessoas2 = []
dados = []

for i, pessoa in enumerate(pessoas):
    for d in pessoa:
        dados.append(d)
  
    pessoas2.append(list(dados))
    dados.clear()
  

print(pessoas2)