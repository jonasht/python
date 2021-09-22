import sqlite3


dados = sqlite3.connect('bancoDeDados.db')
cursor = dados.cursor()

# inserindo dados na tabela
cursor.execute("""
INSERT INTO clientes (nome, idade, email, fone, cidade, uf)
VALUES ('Regis', 35, 'regis@email.com', '11-98765-4321', 'Mogi Guaçu', 'SP')
""")

cursor.execute("""
INSERT INTO clientes (nome, idade, email, fone, cidade, uf)
VALUES ('Aloisio', 87, 'aloisio@email.com', '98765-4322', 'Itapira', 'SP')
""")

cursor.execute("""
INSERT INTO clientes (nome, idade, email, fone, cidade, uf)
VALUES ('Bruna', 21, 'bruna@email.com', '21-98765-4323', 'Estiva Gerbi', 'SP')
""")

cursor.execute("""
INSERT INTO clientes (nome, idade, email, fone, cidade, uf)
VALUES ('Matheus', 19, 'matheus@email.com', '11-98765-4324', 'Mogi Mirim', 'SP')
""")

# gravando no bd
dados.commit()

print('Dados inseridos com sucesso.')

dados.close()
