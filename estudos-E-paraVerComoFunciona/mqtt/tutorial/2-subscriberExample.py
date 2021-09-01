import paho.mqtt.client as mqtt

# este eh o subscriber/subescritor

def on_connect(client, userdata, flags, rc):
    print(f"conectado com code result: {rc}")
    client.subscribe('topic/test')

def on_message(client, userdata, flags, rc):
    if msg.paylod.decode() = 'ola mundo':
        print('sim')
        client.disconnect()


client = mqtt.Client()
client.connect("THE_IP_ADDRESS_OF_OUR_BROKER",1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()