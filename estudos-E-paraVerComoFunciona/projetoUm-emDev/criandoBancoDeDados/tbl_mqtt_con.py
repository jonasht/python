import sqlite3



banco = sqlite3.connect('bancoDeDados.db')

cursor = banco.cursor()


cursor.execute("""CREATE TABLE tbl_mqtt_con (
    serverIP text, 
    serverPort interger, 
    serverClientID text, 
    serverUsername text, 
    serverPassword text, 
    serverPubTopic
    )""")


banco.commit()