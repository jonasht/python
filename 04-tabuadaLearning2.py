from tkinter import *
import random
t = Tk()
t.title('FTabuada v1')
t.iconbitmap('04/ico.ico')
conta_1 = 2
conta_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c = 0
incorreto = correto = 0

def Start():
    conta_total = [conta_1 * conta_2[0], (conta_1 * conta_2[0]) + 2, (conta_1 * conta_2[c]) * 7  ]
    random.shuffle(conta_total)
    lb_conta.config(text=str(conta_1) + ' X ' + str(conta_2[0]))
    bt0.config(text=conta_total[0], state=NORMAL)
    bt1.config(text=conta_total[1], state=NORMAL)
    bt2.config(text=conta_total[2], state=NORMAL)
    
    bt_start.config(state=DISABLED, fg='white', bg='white')
    
    
def comando(res_comando):
    global conta_total
    global conta_1
    global conta_2
    global c
    global correto
    global incorreto
    
    if c <= len(conta_2):
        c = c + 1
    
    
    conta_total = [conta_1 * conta_2[c], (conta_1 * conta_2[c]) + 7,(conta_1 * conta_2[c]) * 7 ]
    random.shuffle(conta_total)
    lb_conta.config(text=str(conta_1) + ' X ' + str(conta_2[c]))
    
    lb_conta_resposta.config(text=str(conta_1) + ' X ' + str(conta_2[c-1]) + ' = ' + str(conta_1 * conta_2[c-1]))
    
    bt0.config(text=conta_total[0], state=NORMAL)
    bt1.config(text=conta_total[1], state=NORMAL)
    bt2.config(text=conta_total[2], state=NORMAL)
    
    if (conta_1 * conta_2[c]) == conta_total[res_comando]:
        lb_resposta.config(text='correto')
        correto = correto + 1
        lb_correto.config(text=correto)
    else:
        lb_resposta.config(text='incorreto')
        incorreto = incorreto + 1
        lb_incorreto.config(text=incorreto)

lb_conta = Label(t, text='=-=-=-=', width=5, fg='red', font='arial 80 bold')

lb_resposta = Label(t, text='=-=-=-=-=-=', fg='blue', font='arial 20 bold')
lb_conta_resposta = Label(t, text='=-=-=-=-=-=', fg='dark blue', font='arial 20 bold')
bt0 = Button(t, text='', command=lambda: comando(0), state=DISABLED, font='arial 20 bold', 
             width=5, borderwidth=2)
bt1 = Button(t, text='', command=lambda: comando(1), state=DISABLED, font='arial 20 bold', 
             width=5, borderwidth=2)
bt2 = Button(t, text='', command=lambda: comando(2), state=DISABLED, font='arial 20 bold', 
             width=5, borderwidth=2)



lb_conta.grid(row=0, columnspan=3, sticky=W+E)
lb_resposta.grid(row=1, column=1,columnspan=2, sticky=W+E)
lb_conta_resposta.grid(row=2, column=1,columnspan=2, sticky=W+E)
bt_start = Button(t, text='start', command=Start, font='arial 20')
bt0.grid(row=1, sticky=W+E)
bt1.grid(row=2, sticky=W+E)
bt2.grid(row=3, sticky=W+E)
bt_start.grid(row=4, columnspan=3, sticky=W+E)

lb_correto = Label(t, text=0, fg='blue', font='arial 20 bold')
lb_incorreto = Label(t, text=0, fg='red', font='arial 20 bold')

lb_incorreto.grid(row=3, column=1)
lb_correto.grid(row=3, column=2)


t.mainloop()