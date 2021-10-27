import sqlite3 as sql


banco = sql.connect('DB.db')

cursor = banco.cursor()

banco.commit()
banco.close()