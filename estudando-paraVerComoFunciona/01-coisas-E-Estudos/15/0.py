import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Button

def janela_login():
    sg.theme('Reddit')
    layout = [[sg.Text('nome')], [sg.Input()], [sg.Button('Continuar')]]
    Layout=layout
    return sg.Window('Login', Layout, finalize=True)

def janela_pedido():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Fazer Pedido')],
        [sg.Checkbox('pizza pepperoni', key = 'pizza1'), sg.Checkbox(
            'pizza de queijo', key = 'pizza2')],
        [sg.Button('Voltar'),sg.Button('Fazer Pedido')]
    ]
    Layout=layout
    return sg.Window('Montar Pedido', Layout, finalize=True)


janela1, janela2 = janela_login(), None

while True:
    window, event, values = sg.read_all_windows()
    
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    
    if window == janela1 and event == 'Continuar':
        janela2 = janela_pedido()
        janela1.hide()
    
    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()
        
    if window == janela2 and event == 'Fazer Pedido':
        if values['pizza1'] == True and values['pizza2'] == True:
            sg.popup('foram solitados uma pizza Pepperoni e uma pizza de queijo')
        elif values['pizza1'] == True:
            sg.popup('foi solicitado uma pizza pepperoni')
        
        elif values['pizza2'] == True:
            sg.popup('foi solicitado uma pizza de queijo')
        else:
            sg.popup('não foi solitado nenhuma pizza')


