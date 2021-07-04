import keyboard

print('\napertando A ')
qtd_apertos = 0
while True:
    
    if keyboard.is_pressed('a'):
        qtd_apertos += 1
        
        print('A foi apertado ', qtd_apertos)
    if keyboard.is_pressed('s'):
        print('\nfim de programa')
        break
    
    