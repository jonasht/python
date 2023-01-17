from colorama.ansi import *


def toDuo(number):
    number = str(number)
    for n in number:
        if n.isnumeric() or n =='a'or n =='b':
            pass
        else:
            return False
    return True

def toDuo2(number):
    number = str(number)
    for n in number:
        if not(n.isnumeric() or n =='a' or n =='b'):
            return False
    return True

def toDuo3(nums: str) -> bool:
    
    # resultado = filter(lambda n: not(n.isnumeric() or n =='a' or n =='b'), nums)
    r = list(filter(lambda n: not n.isnumeric() and n not in ['a', 'b'], nums))
    return False if r else True 

print(f'{Fore.YELLOW}======================== {Fore.GREEN}True {Fore.YELLOW}======================== {Fore.RESET}')
var='123'
print(f'{Back.BLUE}{var:>30}:{Back.RESET} {Fore.GREEN}{toDuo3(var)}{Fore.RESET}')

var='123a'
print(f'{Back.BLUE}{var:>30}:{Back.RESET} {Fore.GREEN}{toDuo3(var)}{Fore.RESET}')

var='123ba'
print(f'{Back.BLUE}{var:>30}:{Back.RESET} {Fore.GREEN}{toDuo3(var)}{Fore.RESET}')

var='a'
print(f'{Back.BLUE}{var:>30}:{Back.RESET} {Fore.GREEN}{toDuo3(var)}{Fore.RESET}')

print(f'{Fore.YELLOW}======================== {Fore.RED}False {Fore.YELLOW}======================== {Fore.RESET}')

var='1z3ba'
print(f'{Back.BLUE}{var:>30}:{Back.RESET} {Fore.RED}{toDuo3(var)}{Fore.RESET}')

var='zzzz'
print(f'{Back.BLUE}{var:>30}:{Back.RESET} {Fore.RED}{toDuo3(var)}{Fore.RESET}')

var='asfsadf'
print(f'{Back.BLUE}{var:>30}:{Back.RESET} {Fore.RED}{toDuo3(var)}{Fore.RESET}')

var='123456790-'
var='123456790 .'
var= 11.2

print(f'{Back.BLUE}{var:>30}:{Back.RESET} {Fore.RED}{toDuo3(var)}{Fore.RESET}')

print()


def teste1():
    print('123:', toDuo(123))
    print('20a:', toDuo('20a'))

    # var='123ba'
    # print(f'{var}:', toDuo(var))

    # var='1z3ba'
    # print(f'{var}:', toDuo(var))

    var='zzzz'
    print(f'{var}:', toDuo(var))

    var='a'
    print(f'{var}:', toDuo(var))