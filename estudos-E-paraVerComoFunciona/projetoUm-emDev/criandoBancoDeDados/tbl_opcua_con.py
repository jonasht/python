import sqlite3



banco = sqlite3.connect('bancoDeDados.db')

cursor = banco.cursor()

cursor.execute("""
               CREATE TABLE tbl_opcua_general (
                   delayBetweenScan interger
               )
               """)

banco.commit()
banco.close()