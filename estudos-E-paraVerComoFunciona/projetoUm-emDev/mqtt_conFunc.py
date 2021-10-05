import sqlite3




def set_serverIP(ip):

    banco = sqlite3.connect('bancoDeDados.db')
    cursor = banco.cursor()

    cursor.execute("""
                   UPDATE tbl_mqtt_con 
                   SET serverIP = ?
                   """, (ip, ))
    banco.commit()
    banco.close()
    
def get_serverIP():
    banco = sqlite3.connect('bancoDeDados.db')
    cursor = banco.cursor()
    cursor.execute('SELECT serverIP FROM tbl_mqtt_con')
    retornar = cursor.fetchall()
    banco.commit()
    banco.close()
    return retornar[0][0]


def set_serverPort(port):
    banco = sqlite3.connect('bancoDeDados.db')
    cursor = banco.cursor()

    cursor.execute("""
                   UPDATE tbl_mqtt_con 
                   SET serverPort = ?
                   """, (port, ))
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

def set_serverClientID(id):
    banco = sqlite3.connect('bancoDeDados.db')
    cursor = banco.cursor()
    
    cursor.execute("""
                UPDATE tbl_mqtt_con 
                SET serverClientID = ?
                """, (id, ))
    banco.commit()
    banco.close()
        
def get_serverClientID():
    banco = sqlite3.connect('bancoDeDados.db')
    cursor = banco.cursor()
    
    cursor.execute('SELECT serverClientID FROM tbl_mqtt_con')
    retornar = cursor.fetchall()
    banco.commit()
    banco.close()
    return retornar[0][0]


# cursor.execute("""CREATE TABLE tbl_mqtt_con (
#     serverIP text, 
#     serverPort interger, 
#     serverClientID text, 
#     serverUsername text, 
#     serverPassword text, 
#     serverPubTopic
#     )""")

def set_serverUsername(name):
    banco = sqlite3.connect('bancoDeDados.db')
    cursor = banco.cursor()
    cursor.execute("""
                UPDATE tbl_mqtt_con 
                SET serverUsername = ?
                """, (name, ))      
    banco.commit()
    banco.close()
def get_serverUsername():
    banco = sqlite3.connect('bancoDeDados.db')
    cursor = banco.cursor()
    cursor.execute('SELECT serverUsername FROM tbl_mqtt_con')
    retornar = cursor.fetchall()
    banco.commit()
    banco.close()
    return retornar[0][0]
     

def set_serverPassword(password):
    banco = sqlite3.connect('bancoDeDados.db')
    cursor = banco.cursor()
    cursor.execute("""
                UPDATE tbl_mqtt_con 
                SET serverPassword = ?
                """, (password, ))
    banco.commit()
    banco.close()     
    
def get_serverPassword():
    banco = sqlite3.connect('bancoDeDados.db')
    cursor = banco.cursor()
    cursor.execute('SELECT serverPassword FROM tbl_mqtt_con')
    retornar = cursor.fetchall()
    banco.commit()
    banco.close()
    return retornar[0][0]
      

def set_serverPubTopic(topic):
    banco = sqlite3.connect('bancoDeDados.db')
    cursor = banco.cursor()
    cursor.execute("""
                UPDATE tbl_mqtt_con 
                SET serverPubTopic = ?
                """, (topic, )) 
    banco.commit()
    banco.close()
         
def get_serverPubTopic():
    banco = sqlite3.connect('bancoDeDados.db')
    cursor = banco.cursor()
    cursor.execute('SELECT serverPubTopic FROM tbl_mqtt_con')
    retornar = cursor.fetchall()
    banco.commit()
    banco.close()
    return retornar[0][0]
      

def mostrar():
    banco = sqlite3.connect('bancoDeDados.db')
    cursor = banco.cursor()
    cursor.execute('SELECT * FROM tbl_mqtt_con')
    print(cursor.fetchall())
    banco.commit()
    banco.close()

if __name__ == '__main__':
    set_serverIP('localhost')
    # print(get_serverIP())    
    mostrar()
