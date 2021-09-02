import sqlite3

banco = sqlite3.connect('primeiro_banco.db')

cursor = banco.cursor()

cursor.execute("INSERT INTO pessoas VALUES('anderson', 18, 'anderson@outlook.com')")



banco.commit()
