import colorama 
colorama.init()
def l(): print(b, 20*'=-'+'=')
r = '\033[31m' # red
b = '\033[34m' # blue
f = '\33[m'
dict = {
    '-English-': '-Portugues-',
    'book': 'livro',
    'if': 'se'
    
    }
l()

print(r, dict['book'])
print(b, dict['if'])

l()