from opcua import Client
from uteis import *

from random import randint
from time import sleep
from paho.mqtt import client as mqtt_client
from uteis import get_Pessoas

# opcua   ---------------------------------------------------
# ip local do cliente
url = 'opc.tcp://localhost:4840' 

client_op = Client(url)
client_op.connect()

print(Fore.GREEN, 'cliente conectado')
print(' client connected ', Fore.RESET)

# mqtt -------------------------------------
broker = 'localhost'
port = 1883
topic = 'teste'


# gerando client id com pub prefixo aleatorio
client_id = f'python-mqtt-{randint(0, 1000)}'

username = 'teste'
password = '123'



def connect_mqtt():

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.connect(broker, port)
    return client


def run():
    client = connect_mqtt()
    client.loop_start()
    

    while True:
        sleep(1)
        Dados = client_op.get_node('ns=2;i=2')
        dados = Dados.get_value()
        client.publish(topic, dados)



if __name__ == '__main__':
    run()
    
