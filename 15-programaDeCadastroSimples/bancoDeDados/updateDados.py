import sqlite3

conn = sqlite3.connect('bancoDeDados.db')
cursor = conn.cursor()

id_cliente = 1
novo_nome ='Carlos'
nova_idade = 20

# alterando os dados da tabela
cursor.execute("""
UPDATE clientes
SET sexo = ?, idade = ?
WHERE id = ?
""", (novo_nome, nova_idade, id_cliente))

conn.commit()

print('Dados atualizados com sucesso.')

conn.close()
