from tkinter import *

t = Tk()
conta_1 = 1
conta_2 = 10
def comando():
    global conta_total
    global conta_1
    global conta_2
    
    lb_conta.config(text=str(conta_1) + ' X ' + str(conta_2))
    bt.config(text='reposta')
    
    
lb_conta = Label(t, text='-=-=-=-=', fg='red', font='arial 80 bold')

lb_resposta = Label(t, text='-=-=-=-=', fg='blue')

bt = Button(t, text='start', command=comando)


lb_conta.grid(row=0, columnspan=2)
lb_resposta.grid(row=1, column=1, sticky=W+E)
bt.grid(row=1, sticky=W+E)

t.mainloop()