import keyboard
from os import system

msns = []
select = 0

def option(*p, op=1):
    global select
    if op == 1 and p != '':
        msns.extend(p)
    if op == 0:
        print('\n')
        system('clear')
        for i, msn in enumerate(msns):
            if i == select:
                print(f'> {i} {msn}')
            else:
                print(f'  {i} {msn}')


print('\n')
option('fazer algo', 'fazer outro algo', 'fazer algo outro')
option('fazer algo', 'fazer algo outro')
option(op=0)
#keyboard.add_hotkey('w', up)

def up():
    global select
    if select == 0:
        return
    select -= 1
    option(op=0)

def down():
    global select
    if select == 4:
        return
    select += 1
    option(op=0)
def enter():
    print('voce escolheu a opcão', select)

keyboard.add_hotkey('up', up)
keyboard.add_hotkey('down', down)
keyboard.add_hotkey('w', up)
keyboard.add_hotkey('s', down)
keyboard.add_hotkey('enter', enter)
keyboard.wait()
