import sqlite3

def mostrar_produtos():
    dados = sqlite3.connect('bancoDeDados.db')
    cursor = dados.cursor()

    # lendo os dados
    cursor.execute("SELECT * FROM produtos;")

    for linha in cursor.fetchall():
        print(linha)

    dados.close()

def cadastrar_produto(nome, quantidade=0, tamanho='', cor=''):
    
    
    
    dados = sqlite3.connect('bancoDeDados.db')
    cursor = dados.cursor()

    cursor.execute("""
                   INSERT INTO produtos(nome, quantidade, tamanho, cores)
                   VALUES (?, ?,?,?)
                   """, (nome, quantidade, tamanho, cor))
    dados.commit()
    dados.close()


# cadastrar_produto(nome='bone', cor='vermelho', quantidade=2)
# mostrar_produtos()