import sqlite3



def set_delayBetweenScan(delay):
    banco = sqlite3.connect('bancoDeDados.db')
    cursor = banco.cursor() 
    cursor.execute("""
                   UPDATE tbl_opcua_general
                   SET delayBetweenScan = ?
                   """, (delay, ))
    banco.commit()
    banco.close()

def get_delayBetweenScan():
    banco = sqlite3.connect('bancoDeDados.db')
    cursor = banco.cursor()
    cursor.execute('SELECT delayBetweenScan FROM tbl_opcua_general')
    retornar = cursor.fetchall()
    banco.commit()
    banco.close()
    return retornar[0][0]
 
    
def mostrar():
    banco = sqlite3.connect('bancoDeDados.db')
    cursor = banco.cursor()
    cursor.execute('SELECT * FROM tbl_opcua_general')
    print(cursor.fetchall())
    banco.commit()
    banco.close()

    
if __name__ == '__main__':
    set_delayBetweenScan(1)    
    print(get_delayBetweenScan())
    mostrar()