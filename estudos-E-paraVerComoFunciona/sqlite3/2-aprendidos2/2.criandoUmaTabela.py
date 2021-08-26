import sqlite3
from colorama.ansi import Fore as fg


# conectando
banco = sqlite3.connect('clientes.db')


cursor = banco.cursor()

# criando uma tabela(schema)
cursor.execute("""
               CREATE TABLE clientes (
                   id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,idade INTEGER,cpf VARCHAR(11) NOT NULL,
                   email TEXT NOT NULL,
                   fone TEXT,
                   cidade TEXT,uf VARCHAR(2) NOT NULL,
                   criado_em DATE NOT NULL
                   );
                   """)


print(f'tabela crianda com {fg.GREEN}sucesso{fg.RESET}')

# desconectando
banco.close()

