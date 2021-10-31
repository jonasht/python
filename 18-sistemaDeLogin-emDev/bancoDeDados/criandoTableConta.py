import sqlite3 as sql 

dados = sql.connect('db.db')

cursor = dados.cursor()

cursor.execute("""
                CREATE TABLE conta (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    sobrenome TEXT,
                    login TEXT,
                    senha TEXT, 
                    email TEXT,
                    frase TEXT
                );
               """)

dados.commit()
dados.close()

