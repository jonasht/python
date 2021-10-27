from os import getpid
import sqlite3
from sqlite3.dbapi2 import Cursor

from maquina import Maquina

def add_(name=None, ip=None, url=None):
    banco = sqlite3.connect('bancoDeDados.db')
    cursor = banco.cursor()

    cursor.execute("""
                   INSERT INTO tbl_opcua_machines (name, ip, url) VALUES(?, ?, ?)
                   """, (name, ip, url))
    
    banco.commit()
    banco.close()

    
    

    
    
def get_name(nomeMaquina):
    banco = sqlite3.connect('bancoDeDados.db')
    cursor = banco.cursor()    
    cursor.execute("""
                   SELECT name FROM tbl_opcua_machines WHERE name = ?
                   """, (nomeMaquina, ))
    retornar = cursor.fetchall()
    banco.commit()
    banco.close()
    return retornar[0][0] 


      
def get_ip(maquina):
    banco = sqlite3.connect('bancoDeDados.db')
    cursor = banco.cursor()      
    cursor.execute("""
                   SELECT ip FROM tbl_opcua_machines WHERE name = ?
                   """, (maquina, ))
    retornar = cursor.fetchall()
    banco.commit()
    banco.close()
    return retornar[0][0]

 
def update_ip(nomeMaquina, ip):
    banco = sqlite3.connect('bancoDeDados.db')
    cursor = banco.cursor()        
    cursor.execute("""
                   UPDATE tbl_opcua_machines 
                   SET ip = ?
                   WHERE name = ?
                   """, (ip, nomeMaquina))  
    banco.commit()
    banco.close()
    
def update_name(nomeMaquina, name):
    banco = sqlite3.connect('bancoDeDados.db')
    cursor = banco.cursor()        
    cursor.execute("""
                   UPDATE tbl_opcua_machines 
                   SET name = ?
                   WHERE name = ?
                   """, (name, nomeMaquina))  
    banco.commit()
    banco.close()
    
def update_url(maquina, url):
    banco = sqlite3.connect('bancoDeDados.db')
    cursor = banco.cursor()       
    cursor.execute("""
                   UPDATE tbl_opcua_machines 
                   SET url = ?
                   WHERE name = ?
                   """, (url, maquina))  
    banco.commit()
    banco.close()
    
def get_url(maquina): 
    banco = sqlite3.connect('bancoDeDados.db')
    cursor = banco.cursor()     
    cursor.execute("""
                   SELECT url FROM tbl_opcua_machines WHERE name = ?
                   """, (maquina, ))
    retornar = cursor.fetchall()
    banco.commit()
    banco.close()
    return retornar[0][0]    
   
def mostrar():
    banco = sqlite3.connect('bancoDeDados.db')
    cursor = banco.cursor()    
    cursor.execute('SELECT * FROM tbl_opcua_machines')
    print(cursor.fetchall())
    banco.commit()
    banco.close()



if __name__ == '__main__':
    maquina = 'maquina1'
    print(get_ip(maquina='maquina1'))
    update_url(maquina, '127.0.0.1')
    mostrar()

