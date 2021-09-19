import sqlite3
from colorama.ansi import Fore as fore

nome = 'fernando'
idade = 18
email = 'fernando@gmail.com'


banco = sqlite3.connect('primeiro_banco.db')

cursor = banco.cursor()

cursor.execute(f"INSERT INTO pessoas VALUES ('{nome}', {idade}, '{email}')")

banco.commit()

print(f'dados inserindos com {fore.GREEN}sucesso{fore.RESET}')