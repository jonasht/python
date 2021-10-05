import sqlite3

import sqlite3

banco = sqlite3.connect('bancoDeDados.db')

cursor = banco.cursor()

# criando table 
cursor.execute("CREATE TABLE pessoas (nome text, idade integer, email text)")


cursor.execute("INSERT INTO pessoas VALUES('maria', 40, 'maria@outlook.com')")
cursor.execute("INSERT INTO pessoas VALUES('joao', 45, 'joao@outlook.com')")
cursor.execute("INSERT INTO pessoas VALUES('jonas', 25, 'jonas@outlook.com')")
cursor.execute("INSERT INTO pessoas VALUES('marcelo', 25, 'marcelo@gmail.com')")

cursor.execute("INSERT INTO pessoas VALUES('sonia', 54 , 'sonia@gmail.com')")
cursor.execute("INSERT INTO pessoas VALUES('douglas', 45, 'douglas@gmail.com')")
cursor.execute("INSERT INTO pessoas VALUES('marcos', 52, 'marcos@gmail.com')")


banco.commit()

cursor.execute("SELECT * FROM pessoas")
print(cursor.fetchall())