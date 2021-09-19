from paho.mqtt import client as mqtt_client
from uteis import *

broker = 'localhost'
port = 1883
topic = 'teste'


# gerando client id com pub prefixo aleatorio
client_id = f'python-mqtt-{randint(0, 1000)}'

# usuario e senha
username = 'teste'
password = '123'

# pegando dados s
pessoas = get_Pessoas()

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
    while True:
        sleep(1)

        for pessoa in pessoas:
            mensagem = ''
            for dados in pessoa:
                mensagem += f'{dados} '
            resultado = client.publish(topic, mensagem)

            status = resultado[0]
            if status != 0:
                print(f"Failed to send message to topic {topic}")
                print(f'falha ao enviar a mensagem ao topic {topic}')


def on_message(client, userdata, msg):
    print(f'{Fore.BLUE}-->{Fore.GREEN} {msg.payload.decode()} {Fore.BLUE}do topico{msg.topic}{Fore.RESET} ')
    
def run():
    # subscriber ----------------
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)

    client.on_message = on_message
    client.connect(broker, port)
    client.subscribe(topic)
    client.loop_forever()
    
    # publisher -------------
    client = connect_mqtt()
    client.loop_start()
    publish(client)


    
if __name__ == '__main__':
    run()
    


