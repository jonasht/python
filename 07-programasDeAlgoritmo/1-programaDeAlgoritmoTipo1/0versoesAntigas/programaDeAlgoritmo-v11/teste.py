# versão 10, versao o que ha de novo:
# a cor amarela para retroceder
# quando terminar a ultima cor some 
from algoritmo2 import *

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# definir de tamanho, o tempo e o pixel de character
# M2(tamanho, tempo, tamanho do pixel ou oque vai estar nele)

pr = M2(64, .1, "   ")
# pr = M2(30, .05, "   ")



# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# se aparecer tudo errado, tem que diminuir a fonte do terminal (ctrl + -)
# também se aparecer tudo errado mostrar [alguma coisa, o terminal não suporta ansii
# o codigo foi feito no gnu/linux, caso for no windows deve-se importar colorama

# import colorama
# colorama.init()

# para instalar colorama no windows
# pip install colorama
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
pr.Maneira2()   
