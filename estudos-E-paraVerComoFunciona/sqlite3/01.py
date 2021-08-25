import sqlite3

banco = sqlite3.connect('primeiro_banco.db')

cursor = banco.cursor()

cursor.execute("CREATE TABLE pessoas (nome text, idade integer, email text)")

cursor.execute("INSERT INTO pessoas VALUES('maria', 40, 'maria@outlook.com')")
cursor.execute("INSERT INTO pessoas VALUES('joao', 45, 'joao@outlook.com')")
cursor.execute("INSERT INTO pessoas VALUES('jonas', 25, 'jonas@outlook.com')")



banco.commit()

cursor.execute("SELECT * FROM pessoas")
print(cursor.fetchall())