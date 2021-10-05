import sqlite3


banco = sqlite3.connect('bancoDeDados.db')

cursor = banco.cursor()
# id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT
# foi colocado

cursor.execute(
    """
    CREATE TABLE tbl_opcua_machines (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name text,
        ip text,
        url text
    )
    """
)

banco.commit()
banco.close()

