import sqlite3



dados = sqlite3.connect('bancoDeDAdos.db')
cursor = dados.cursor()
# dados.commit()


# SELECIONANDO tudo DE pessoas
# def 
cursor.execute("SELECT * FROM pessoas")
print(cursor.fetchall())