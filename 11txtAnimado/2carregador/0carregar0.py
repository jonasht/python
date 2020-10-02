from time import sleep
def carregador():

    for i in range(51):
        print(f'[{(i*2):<3}%] [{("#" * i):>}{("." * (51-i-1))}]', flush=True)
        
        sleep(.03)
    print()
carregador()