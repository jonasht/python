from cryptography.fernet import Fernet


def criptar(msg):

    key = Fernet.generate_key()

    f = Fernet(key)
    
    token = f.encrypt(msg.encode())
    
    # convertendo para string
    key = key.decode('utf-8')
    token = token.decode('utf-8')
    return key, token

def descriptar(key, t):
    key = key.encode()
    print()
    print('tipo:', type(t))

    print('t:', t)
    t = t.encode()
    f = Fernet(key)
    msg = f.decrypt(t)
    
    msg = msg.decode('utf-8')

    return msg
    
    

if __name__ == '__main__':
        
    key = 'qy2OA1nnLPzM0Uj3Qyg5qdY8Nn7hzUVOWXliHmsDvms='
    msg = 'gAAAAABiI9KBWEVn9aZlGx7lQvx-xmSFs5uLMU6KTU7ACmpUPIVD99NVMVKwzykwOJ8hloHG2T1jBIRCfVRRImFxhEgK6XwL5A=='
    print(descriptar(key, msg))