import sqlite3



def add_variableName(variable):
    banco = sqlite3.connect('bancoDeDados.db')
    cursor = banco.cursor()

    cursor.execute("""
                   INSERT INTO tbl_opcua_data (variableName) VALUES (?)
                   """, (variable, ))
    banco.commit()
    banco.close()
        
def get_variableName():
    banco = sqlite3.connect('bancoDeDados.db')
    cursor = banco.cursor()

    cursor.execute('SELECT variableName FROM tbl_opcua_data')
    retornar = cursor.fetchall()
    return retornar[0][0]

def add_ns(ns):
    banco = sqlite3.connect('bancoDeDados.db')
    cursor = banco.cursor()
 
    cursor.execute("""
        INSERT INTO tbl_opcua_data(ns) VALUES(?)
    """, (ns, ))
    banco.commit()
    banco.close()
    
def get_ns():
    banco = sqlite3.connect('bancoDeDados.db')
    cursor = banco.cursor()    
    
    cursor.execute('SELECT ns FROM tbl_opcua_data')
    retornar = cursor.fetchall()
        
    banco.commit()
    banco.close()

    return retornar[0][0]    

def add_type(type):
    banco = sqlite3.connect('bancoDeDados.db')
    cursor = banco.cursor()

    cursor.execute("""
        INSERT INTO tbl_opcua_data(type) VALUES(?)
    """, (type, ))
    banco.commit()
    banco.close()
    
def get_type():
    banco = sqlite3.connect('bancoDeDados.db')
    cursor = banco.cursor()    

    cursor.execute('SELECT type FROM tbl_opcua_data')
    retornar = cursor.fetchall()
    banco.commit()
    banco.close()

    return retornar[0][0]

def mostrar():
    banco = sqlite3.connect('bancoDeDados.db')
    cursor = banco.cursor()

    cursor.execute('SELECT * FROM tbl_opcua_data')
    print(cursor.fetchall())
    
def add_(variableName, ns, type):
    add_variableName(variableName)
    add_ns(ns)
    add_type(type)
    
# cursor.execute("INSERT INTO pessoas VALUES('anderson', 18, 'anderson@outlook.com')")
if __name__ == '__main__':
    mostrar()
    print()
    add_variableName('algo')
    print(get_variableName())




