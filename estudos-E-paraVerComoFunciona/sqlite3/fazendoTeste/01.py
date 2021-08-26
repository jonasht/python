import sqlite3

banco = sqlite3.connect('bancoDeDAdos.db')

cursor = banco.cursor()

# criando table pessoas, com nome idade email
cursor.execute("CREATE TABLE pessoas (nome text, idade integer, email text)")

# =============================================================================
cursor.execute("INSERT INTO pessoas VALUES('maria', 40, 'maria@outlook.com')")
cursor.execute("INSERT INTO pessoas VALUES('joao', 45, 'joao@outlook.com')")
cursor.execute("INSERT INTO pessoas VALUES('jonas', 25, 'jonas@outlook.com')")
cursor.execute("INSERT INTO pessoas VALUES('carlos', 54, 'carlos@outlook.com')")
cursor.execute("INSERT INTO pessoas VALUES('marcelo', 20, 'marcelo@outlook.com')")


# mandando para o banco
banco.commit()

