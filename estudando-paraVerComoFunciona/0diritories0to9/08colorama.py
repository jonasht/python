
'''
pip install colorama
python -m pip install colorama
'''
from colorama import *
init()

print('hello world')

print(Fore.RED+'isso deve ser vermelho.')
print(Fore.GREEN+'isso deve ser verde')


print(Back.WHITE+'isso deve ter background branco.')
print(Style.RESET_ALL+'isso deve texto normal')

print("\033[31m" + " algo algo algo")



