from random import randint
from time import sleep
from paho.mqtt import client as mqtt_client


broker = 'localhost'
port = 1883
topic = 'teste'


# gerando client id com pub prefixo aleatorio
client_id = f'python-mqtt-{randint(0, 1000)}'

username = 'teste'
password = '123'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print('Connected to MQTT Broker!')
            print('conectado ao MQTT Broker')
        else:
            print("Failed to connect, return code %d\n", rc)
            print(f'Falha para conectar, retorne codigo {rc}')
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client):
    msg_count = 0
    while True:
        sleep(1)
        msg = f'mensagem: {msg_count}'
        result = client.publish(topic, msg)
 
        status = result[0]
        if status == 0:
            print(f'Send {msg} to topic {topic}')
            print(f'enviando {msg} ao topico {topic}')
        else:
            print(f"Failed to send message to topic {topic}")
            print(f'falha ao enviar a mensagem ao topic {topic}')
        msg_count += 1


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()