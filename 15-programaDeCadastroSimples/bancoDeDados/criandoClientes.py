import sqlite3

dados = sqlite3.connect('bancoDeDados.db')

cursor = dados.cursor()

cursor.execute("""
               CREATE TABLE clientes(
                   id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,
                   sexo TEXT,
                   idade INTERGER
               );
               """)
dados.close()