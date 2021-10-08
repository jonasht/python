import sqlite3






def add_(serverIP=None, serverPort=None, serverClientID=None, serverUsername=None, serverPassword=None, serverPubTopic=None):
    banco = sqlite3.connect('bancoDeDados.db')
    cursor = banco.cursor()    
    cursor.execute("""
                   INSERT INTO tbl_mqtt_con (serverIP, serverPort, serverClientID, serverUsername, serverPassword, serverPubTopic) 
                   VALUES(?, ?, ?, ?, ?, ?)
                   """, (serverIP, serverPort, serverClientID, serverUsername, serverPassword, serverPubTopic))
    banco.commit()
    banco.close()

def get_serverPort():
    banco = sqlite3.connect('bancoDeDados.db')
    cursor = banco.cursor()
    cursor.execute('SELECT serverPort FROM tbl_mqtt_con')
    retornar = cursor.fetchall()
    banco.commit()
    banco.close()
    return retornar[0][0]
def get_serverClientID():
    banco = sqlite3.connect('bancoDeDados.db')
    cursor = banco.cursor()
    
    cursor.execute('SELECT serverClientID FROM tbl_mqtt_con')
    retornar = cursor.fetchall()
    banco.commit()
    banco.close()
    return retornar[0][0]

def get_serverUsername():
    banco = sqlite3.connect('bancoDeDados.db')
    cursor = banco.cursor()
    cursor.execute('SELECT serverUsername FROM tbl_mqtt_con')
    retornar = cursor.fetchall()
    banco.commit()
    banco.close()
    return retornar[0][0]

def get_serverPassword():
    banco = sqlite3.connect('bancoDeDados.db')
    cursor = banco.cursor()
    cursor.execute('SELECT serverPassword FROM tbl_mqtt_con')
    retornar = cursor.fetchall()
    banco.commit()
    banco.close()
    return retornar[0][0]

def get_serverPubTopic():
    banco = sqlite3.connect('bancoDeDados.db')
    cursor = banco.cursor()
    cursor.execute('SELECT serverPubTopic FROM tbl_mqtt_con')
    retornar = cursor.fetchall()
    banco.commit()
    banco.close()
    return retornar[0][0]


def get_serverIP():
    banco = sqlite3.connect('bancoDeDados.db')
    cursor = banco.cursor()    
    cursor.execute("""
                   SELECT serverIP FROM tbl_mqtt_con
                   """) 
    retornar = cursor.fetchall()   
    banco.commit()
    banco.close()
    return retornar[0][0]

def mostrar():
    banco = sqlite3.connect('bancoDeDados.db')
    cursor = banco.cursor()    
    cursor.execute("""
                   SELECT * FROM tbl_mqtt_con
                   """)
    print(cursor.fetchall())
    banco.commit()
    banco.close()

if __name__ == '__main__':
    # add_(serverIP='localhost', serverPort=1883, serverUsername='teste', serverPassword='123', serverPubTopic='teste')
    mostrar()
    print('ip:', get_serverIP(), 'port:', get_serverPort(),'clientId:', get_serverClientID(), 'username:', get_serverUsername(), 'password:', get_serverPassword(), 'pubTopic:', get_serverPubTopic())