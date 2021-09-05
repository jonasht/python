import sqlite3

dados = sqlite3.connect('bancoDeDados.db')
cursor = dados.cursor()

cursor.execute("""
               CREATE TABLE produtos (
                   codigo INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,
                   quantidade INTEGER,
                   tamanho TEXT,
                   cores TEXT
               );
               """)

dados.close()