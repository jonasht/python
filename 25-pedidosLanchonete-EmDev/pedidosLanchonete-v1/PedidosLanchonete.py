from tkinter import *
totalConsumo = 0.0
janela = Tk()

lb_total = Label(janela, text='total:')
lb_total.grid(row=0)
def Consumir(numero_consumo):
    global totalConsumo
    
    if numero_consumo == 1:
        totalConsumo = totalConsumo + 12
    if numero_consumo == 2:
        totalConsumo = totalConsumo + 11
    if numero_consumo == 3:
        totalConsumo = totalConsumo + 13
    if numero_consumo == 4:
        totalConsumo = totalConsumo + 1
    lb_total.config(text='total: ' + str(totalConsumo))
frame_consumo = Frame(janela)
frame_consumo.grid(row=1, column=0)

bt_consumo1 = Button(frame_consumo, text='pastel de carne 12,00', padx=20, pady=20, command=lambda: Consumir(1))
bt_consumo2 = Button(frame_consumo, text='pastel de frago 11,00', padx=20, pady=20, command=lambda: Consumir(2))
bt_consumo3 = Button(frame_consumo, text='pastel de queijo 13,00', padx=20, pady=20, command=lambda: Consumir(3))
bt_consumo4 = Button(frame_consumo, text='suco de laranja 1,00', padx=20, pady=20, command=lambda: Consumir(4))


bt_consumo1.grid(row=0) 
bt_consumo2.grid(row=1) 
bt_consumo3.grid(row=2) 
bt_consumo4.grid(row=3) 



janela.mainloop()