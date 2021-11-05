import sqlite3
from colorama.ansi import Fore

def cadastrar(nome, sexo, idade):
    
    
    dados = sqlite3.connect('bancoDeDados.db')
    cursor = dados.cursor()

    # inserindo dados na tabela
    cursor.execute("""
    INSERT INTO clientes (nome, sexo, idade)
    VALUES (?,?,?)
    """, (nome, sexo, idade))

    # gravando no bd
    dados.commit()

    print(f'{Fore.GREEN}Dados inseridos com sucesso.{Fore.RESET}')

    dados.close()

def mostrar_bd():
    dados = sqlite3.connect('bancoDeDados.db')
    cursor = dados.cursor()

    cursor.execute('SELECT * FROM clientes')
    
    for dados in cursor.fetchall():
        for dado in dados:
            print(f'{dado:>10} ', end='')
        print()
        
def get_dados(opcao='*'):
    opcao = str(opcao)
    # colocar id par returnar id
    if opcao=='*':
        dados = sqlite3.connect('bancoDeDados.db')
        cursor = dados.cursor()

        cursor.execute('SELECT * FROM clientes')
        return list(cursor.fetchall())
    elif opcao.isnumeric():
        opcao = int(opcao)
        dados = sqlite3.connect('bancoDeDados.db')
        cursor = dados.cursor()

        cursor.execute('SELECT * FROM clientes WHERE id = ?', (opcao,))
        return list(cursor.fetchall()[0])
        
def get_nextId():
    dados = sqlite3.connect('bancoDeDados.db')
    cursor = dados.cursor()

    cursor.execute('SELECT * FROM clientes')
    return len(cursor.fetchall()) + 1

def update_bd(id, nome='', sexo='', idade=None):
    idade = str(idade)
    dados = sqlite3.connect('bancoDeDados.db')
    cursor = dados.cursor()
    if id:
        dadosAntigos = get_dados(id)
        print(dadosAntigos)
        if not(nome):
            nome = dadosAntigos[1]
        if not(sexo):
            sexo = dadosAntigos[2]
        if not(idade):
            idade = dadosAntigos[3]
        
        dados.execute("""
        UPDATE clientes
        SET nome = ?, sexo = ?, idade = ?
        WHERE id = ?
        """, (nome, sexo, idade, id))

        dados.commit()

        print('Dados atualizados com sucesso.')

        dados.close()

    else:
        print(f'{Fore.RED}eh necessario colocar o id{Fore.RESET}')
        



if __name__ == '__main__':
    
    mostrar_bd()