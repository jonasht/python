import sqlite3
from colorama.ansi import Fore as fore
# deletando registros

try:
    banco = sqlite3.connect('primeiro_banco.db')

    cursor = banco.cursor()


    cursor.execute("DELETE from pessoas WHERE idade = 40")
    
    banco.commit()
    banco.close()
    
    print(f'os dados foram removidos com {fore.GREEN}sucesso{fore.RESET}')
except sqlite3.Error as erro:
    print(f'{fore.RED}erro ao excluir: {erro}{fore.RESET}')