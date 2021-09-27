import sqlite3


banco = sqlite3.connect('bancoDeDados.db')

cursor = banco.cursor()

cursor.execute(
    """
    CREATE TABLE tbl_opcua_machines (
        name text,
        ip text,
        url text
    )
    """
)

banco.commit()
banco.close()

