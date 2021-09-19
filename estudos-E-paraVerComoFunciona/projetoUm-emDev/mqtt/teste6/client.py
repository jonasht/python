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

# pegando dados
pessoas = get_dados()

def run():
    
    # subscriber --------------------------------
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.connect(broker, port)
    
    client.on_message = lambda client, user, msg: print(f'{Fore.BLUE}-->{Fore.GREEN} {msg.payload.decode()} {Fore.BLUE}do topico {msg.topic}{Fore.RESET} ')
    
    client.subscribe(topic)
    client.loop_forever()
    print('aqui')
    
    
    # publisher -----------------------------------
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.connect(broker, port)


    client.loop_start()

    while True:
        sleep(1)
        for pessoa in pessoas:
            print('funcionando')
            mensagem = ''
            for dados in pessoa:
                mensagem += f'{dados} '
            client.publish(topic, mensagem)

            

if __name__ == '__main__':
    run()
    


