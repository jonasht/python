import sqlite3




banco = sqlite3.connect('bancoDeDados.db')

cursor = banco.cursor()

cursor.execute("""
               CREATE TABLE tbl_opcua_data(
                   machineld interger,
                   variableName text,
                   ns interger,
                   type text
               )
               """)



banco.commit()
banco.close()