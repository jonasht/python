import sqlite3 as sql

banco = sql.connect('cliente.db')

banco.close()