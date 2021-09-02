import random
from paho.mqtt import client as mqtt_client


def on_message(client, userdata, msg):
    print(f'recebendo {msg.payload.decode()} do topico{msg.topic} ')
    

def run():
    broker = 'localhost'
    port = 1883
    topic = "teste"
    client_id = f'python-mqtt-{random.randint(0, 100)}'
    username = 'teste'
    password = '123'
    
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)

    
    client.on_message = on_message
    client.connect(broker, port)
    client.subscribe(topic)
    client.loop_forever()
    
if __name__ == '__main__':
    run()