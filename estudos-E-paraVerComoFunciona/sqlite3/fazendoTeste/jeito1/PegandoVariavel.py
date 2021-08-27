import sqlite3

# SELECIONANDO tudo DE pessoas
def get_Pessoas():
    dados = sqlite3.connect('bancoDeDAdos.db')
    cursor = dados.cursor()
    cursor.execute("SELECT * FROM pessoas")
    pessoas = (cursor.fetchall()).copy()
    return pessoas

