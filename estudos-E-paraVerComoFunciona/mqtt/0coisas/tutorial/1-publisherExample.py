import paho.mqtt.client as mqtt

# este eh o publicador

client = mqtt.Client()
client.connect("localhost", 1883, 60)

client.publish("topic/test", "hello world")
client.disconnect()