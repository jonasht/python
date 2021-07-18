import keyboard
def espaço():
    print('espaço apertado')
keyboard.add_hotkey('space', espaço)



keyboard.wait('ESC')