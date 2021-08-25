import sqlite3
from colorama.ansi import Fore as fore

nome = 'fernando'
idade = 18
email = 'fernando@gmail.com'


banco = sqlite3.connect('primeiro_banco.db')

cursor = banco.cursor()

cursor.execute("UPDATE pessoas SET nome = 'rose' WHERE idade = 18")
banco.commit()

print(f'dados inserindos com {fore.GREEN}sucesso{fore.RESET}')